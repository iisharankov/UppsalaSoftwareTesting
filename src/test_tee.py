import itertools
import pytest

from iterators.invalid_iter import InvalidIter
from iterators.valid_iter import ValidIter


@pytest.mark.parametrize("input, expected", [
    ("", ("", "")),
    (iter([]), (iter([]), iter([]))),
    ("abcdef", ("abcdef", "abcdef")),
    (iter(range(10)), (iter(range(10)), iter(range(10)))),
    (iter(ValidIter(100)), (iter(ValidIter(100)), iter(ValidIter(100))))
])
def test_tee_basic_case(input, expected):
    teed = itertools.tee(input)
    for index in range(2):
        assert list(teed[index]) == list(expected[index])


@pytest.mark.parametrize("input, exception_message", [
    (1, "'int' object is not iterable"),
    (min, "'builtin_function_or_method' object is not iterable"),
    (InvalidIter(), "'InvalidIter' object is not iterable")
])
def test_tee_basic_case_invalid_type(input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        itertools.tee(input)
    assert excinfo.value.args[0] == exception_message


@pytest.mark.parametrize("input, n, expected", [
    ("", 0, ()),
    (iter([]), 0, ()),
    ("abcdef", 0, ()),
    (iter(range(10)), 0, ()),
    (iter(ValidIter(100)), 0, ()),
    ("", 1, ("",)),
    (iter([]), 1, (iter([]),)),
    ("abcdef", 1, ("abcdef",)),
    (iter(range(10)), 1, (iter(range(10)),)),
    (iter(ValidIter(100)), 1, (iter(ValidIter(100)),)),
    ("", 2, ("", "")),
    (iter([]), 2, (iter([]), iter([]))),
    ("abcdef", 2, ("abcdef", "abcdef")),
    (iter(range(10)), 2, (iter(range(10)), iter(range(10)))),
    (iter(ValidIter(100)), 2, (iter(ValidIter(100)), iter(ValidIter(100)))),
    ("", 3, ("", "", "")),
    (iter([]), 3, (iter([]), iter([]), iter([]))),
    ("abcdef", 3, ("abcdef", "abcdef", "abcdef")),
    (iter(range(10)), 3, (iter(range(10)), iter(range(10)), iter(range(10)))),
    (iter(ValidIter(100)), 3, (iter(ValidIter(100)), iter(ValidIter(100)), iter(ValidIter(100))))
])
def test_tee_multiple_n(input, n, expected):
    teed = itertools.tee(input, n)
    assert len(teed) == n
    for index in range(n):
        assert list(teed[index]) == list(expected[index])