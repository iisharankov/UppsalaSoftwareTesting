import itertools
import pytest

from iterators.invalid_iter import InvalidIter


def _grouper_to_keys(grouper):
    return [g[0] for g in grouper]

def _grouper_to_groups(grouper):
    return [list(g[1]) for g in grouper]


@pytest.mark.parametrize("keyfunc, data, expected_keys", [
    (lambda x: x, [], []),
    (lambda x: x, [1, 2, 3], [1, 2, 3]),
    (lambda x: x, [1, 2, 2, 2, 3, 3], [1, 2, 3]),
    (lambda x: x, "", []),
    (lambda x: x, "ABC", ["A", "B", "C"]),
    (lambda x: x, "ABBBCC", ["A", "B", "C"]),
])
def test_groupby_basic_case_keys(keyfunc, data, expected_keys):
    grouper = itertools.groupby(data, keyfunc)
    assert _grouper_to_keys(grouper) == expected_keys


@pytest.mark.parametrize("keyfunc, data, expected_groups", [
    (lambda x: x, [], []),
    (lambda x: x, [1, 2, 3], [[1], [2], [3]]),
    (lambda x: x, [1, 2, 2, 2, 3, 3], [[1], [2, 2, 2], [3, 3]]),
    (lambda x: x, "", []),
    (lambda x: x, "ABC", [["A"], ["B"], ["C"]]),
    (lambda x: x, "ABBBCC", [["A"], ["B", "B", "B"], ["C", "C"]]),
])
def test_groupby_basic_case_groups(keyfunc, data, expected_groups):
    grouper = itertools.groupby(data, keyfunc)
    assert _grouper_to_groups(grouper) == expected_groups


@pytest.mark.parametrize("keyfunc, data, exception_message", [
    (lambda x: x, 1, "'int' object is not iterable"),
    (lambda x: x, min, "'builtin_function_or_method' object is not iterable"),
    (lambda x: x, InvalidIter(), "'InvalidIter' object is not iterable")
])
def test_groupby_basic_case_invalid_data(keyfunc, data, exception_message):
    with pytest.raises(TypeError) as excinfo:
        itertools.groupby(data, keyfunc)
    assert excinfo.value.args[0] == exception_message


@pytest.mark.parametrize("keyfunc, data, expected_keys", [
    (lambda x: x % 2, [], []),
    (lambda x: x % 2, [1, 3, 5, 7, 2, 4, 6, 8], [1, 0]),
    (lambda x: x % 2, [1, 2, 3, 4, 5], [1, 0, 1, 0, 1]),
    (lambda x: True, [], []),
    (lambda x: True, [1, 2, 3, 4], [True]),
    (lambda x: True, "ABCDEF", [True]),
])
def test_groupby_different_keyfunc_keys(keyfunc, data, expected_keys):
    grouper = itertools.groupby(data, keyfunc)
    assert _grouper_to_keys(grouper) == expected_keys


@pytest.mark.parametrize("keyfunc, data, expected_groups", [
    (lambda x: x % 2, [], []),
    (lambda x: x % 2, [1, 3, 5, 7, 2, 4, 6, 8], [[1, 3, 5, 7], [2, 4, 6, 8]]),
    (lambda x: x % 2, [1, 2, 3, 4, 5], [[1], [2], [3], [4], [5]]),
    (lambda x: True, [], []),
    (lambda x: True, [1, 2, 3, 4], [[1, 2, 3, 4]]),
    (lambda x: True, "ABCDEF", [["A", "B", "C", "D", "E", "F"]]),
])
def test_groupby_different_keyfunc_groups(keyfunc, data, expected_groups):
    grouper = itertools.groupby(data, keyfunc)
    assert _grouper_to_groups(grouper) == expected_groups
