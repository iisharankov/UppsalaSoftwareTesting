import itertools
import pytest

from iterators.invalid_iter import InvalidIter


@pytest.mark.parametrize("func, input, expected", [
    (pow, iter([]), []),
    (pow, iter([(2, 1)]), [2**1]),
    (pow, iter([(2, 1), (2, 2)]), [2**1, 2**2]),
    (pow, iter([(2, 1), (2, 2), (2, 3)]), [2**1, 2**2, 2**3]),
    (range, iter([]), []),
    (range, iter([(1, 10)]), [range(1,10)]),
    (range, iter([(1, 10), (11, 20)]), [range(1,10), range(11, 20)]),
    (range, iter([(1, 10), (11, 20), (21, 30)]), [range(1,10), range(11, 20), range(21, 30)]),
    (lambda x1, x2, x3: x1 + x2 + x3, iter([]), []),
    (lambda x1, x2, x3: x1 + x2 + x3, iter([(1, 2, 3)]), [6]),
    (lambda x1, x2, x3: x1 + x2 + x3, iter([(1, 2, 3), (4, 5, 6)]), [6, 15]),
    (lambda x1, x2, x3: x1 + x2 + x3, iter([(1, 2, 3), (4, 5, 6), (7, 8, 9)]), [6, 15, 24])
])
def test_starmap_basic_case(func, input, expected):
    mapped = itertools.starmap(func, input)
    assert list(mapped) == expected


@pytest.mark.parametrize("func, input, exception_message", [
    (pow, 1, "'int' object is not iterable"),
    (pow, min, "'builtin_function_or_method' object is not iterable"),
    (pow, InvalidIter(), "'InvalidIter' object is not iterable")
])
def test_starmap_basic_case_invalid_type(func, input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        itertools.starmap(func, input)
    assert excinfo.value.args[0] == exception_message


@pytest.mark.parametrize("func, input, exception_message", [
    (pow, iter([(2, 1), (2,)]), "pow() missing required argument 'exp' (pos 2)"),
    (range, iter([(2, 1), (2, 2, 2, 4), (2, 3)]), "range expected at most 3 arguments, got 4"),
    (lambda x1, x2: x1 + x2, iter([(1, 2), (3, 4, 5)]), "<lambda>() takes 2 positional arguments but 3 were given"),
    (lambda x1, x2, x3: x1 + x2 + x3, iter([(1, 2, 3), (4, 5)]), "<lambda>() missing 1 required positional argument: 'x3'"),
])
def test_starmap_basic_case_invalid_arguments(func, input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.starmap(func, input))
    assert excinfo.value.args[0] == exception_message