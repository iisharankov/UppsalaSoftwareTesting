import itertools
import pytest

@pytest.mark.parametrize("inputs, stop, expected", [
    ([], 1, []),
    ([-3,-2,-1,0,1,2,3], 0, []),
    ([-3,-2,-1,0,1,2,3], 4, [-3,-2,-1,0]),
    ([-3,-2,-1,0,1,2,3], 7, [-3,-2,-1,0,1,2,3]),
    ([-3,-2,-1,0,1,2,3], 100, [-3,-2,-1,0,1,2,3]),
    ([-3,-2,-1,0,1,2,3], None, [-3,-2,-1,0,1,2,3]),
    ([-3.75,-2.666,-1.25,0.1,1.25,2.666,3.75], 4, [-3.75,-2.666,-1.25,0.1]),
    (["a","b","c","d","c","b","a"], 4, ["a","b","c","d"]),
    (["apple","banana","cherry","date","cherry","banana","apple"], 4,
     ["apple","banana","cherry","date"]),
    (["this",34,[],"is",-3.1415,["a","mixed"],97.215,"array",-68,[["!"]]], 6,
     ["this",34,[],"is",-3.1415,["a","mixed"]])
])
def test_islice_stop(inputs, stop, expected):
    assert list(itertools.islice(inputs, stop)) == expected

@pytest.mark.parametrize("inputs, start, stop, expected", [
    ([], 0, 1, []),
    ([-3,-2,-1,0,1,2,3], 0, 0, []),
    ([-3,-2,-1,0,1,2,3], 0, 4, [-3,-2,-1,0]),
    ([-3,-2,-1,0,1,2,3], 4, 0, []),
    ([-3,-2,-1,0,1,2,3], 7, 7, []),
    ([-3,-2,-1,0,1,2,3], 2, 4, [-1,0]),
    ([-3,-2,-1,0,1,2,3], 2, 7, [-1,0,1,2,3]),
    ([-3,-2,-1,0,1,2,3], 2, 100, [-1,0,1,2,3]),
    ([-3,-2,-1,0,1,2,3], None, None, [-3,-2,-1,0,1,2,3]),
    ([-3.75,-2.666,-1.25,0.1,1.25,2.666,3.75], 2, 4, [-1.25,0.1]),
    (["a","b","c","d","c","b","a"], 2, 4, ["c","d"]),
    (["apple","banana","cherry","date","cherry","banana","apple"], 2, 4,
     ["cherry","date"]),
    (["this",34,[],"is",-3.1415,["a","mixed"],97.215,"array",-68,[["!"]]], 2, 6,
     [[],"is",-3.1415,["a","mixed"]])
])
def test_islice_start_stop(inputs, start, stop, expected):
    assert list(itertools.islice(inputs, start, stop)) == expected

@pytest.mark.parametrize("inputs, start, stop, step, expected", [
    ([], 0, 1, 1, []),
    ([-3,-2,-1,0,1,2,3], 0, 0, 1, []),
    ([-3,-2,-1,0,1,2,3], 0, 4, 1, [-3,-2,-1,0]),
    ([-3,-2,-1,0,1,2,3], 4, 0, 1, []),
    ([-3,-2,-1,0,1,2,3], 7, 7, 1, []),
    ([-3,-2,-1,0,1,2,3], 2, 4, 1, [-1,0]),
    ([-3,-2,-1,0,1,2,3], 2, 7, 1, [-1,0,1,2,3]),
    ([-3,-2,-1,0,1,2,3], 2, 100, 1, [-1,0,1,2,3]),
    ([-3,-2,-1,0,1,2,3], None, None, None, [-3,-2,-1,0,1,2,3]),
    ([-3.75,-2.666,-1.25,0.1,1.25,2.666,3.75], 2, 4, 1, [-1.25,0.1]),
    (["a","b","c","d","c","b","a"], 2, 4, 1, ["c","d"]),
    (["apple","banana","cherry","date","cherry","banana","apple"], 2, 4, 1,
     ["cherry","date"]),
    (["this",34,[],"is",-3.1415,["a","mixed"],97.215,"array",-68,[["!"]]], 2, 6, 1,
     [[],"is",-3.1415,["a","mixed"]])
])
def test_islice_start_stop_step_single(inputs, start, stop, step, expected):
    assert list(itertools.islice(inputs, start, stop, step)) == expected

@pytest.mark.parametrize("inputs, start, stop, step, expected", [
    ([-3,-2,-1,0,1,2,3,4,5,6,7,8,9], 0, 9, 3, [-3,0,3]),
    ([-3,-2,-1,0,1,2,3,4,5,6,7,8,9], 2, 9, 3, [-1,2,5]),
    ([-3,-2,-1,0,1,2,3,4,5,6,7,8,9], 2, 13, 3, [-1,2,5,8]),
    ([-3,-2,-1,0,1,2,3,4,5,6,7,8,9], 2, 100, 3, [-1,2,5,8]),
    ([-3,-2,-1,0,1,2,3,4,5,6,7,8,9], None, None, 3, [-3,0,3,6,9]),
    ([-3.75,-2.666,-1.25,0.1,1.25,2.666,3.75], 2, 7, 3, [-1.25,2.666]),
    (["a","b","c","d","c","b","a"], 2, 7, 3, ["c","b"]),
    (["apple","banana","cherry","date","cherry","banana","apple"], 2, 7, 3,
     ["cherry","banana"]),
    (["this",34,[],"is",-3.1415,["a","mixed"],97.215,"array",-68,[["!"]]], 2, 10, 3,
     [[],["a","mixed"],-68])
])
def test_islice_start_stop_step_triple(inputs, start, stop, step, expected):
    assert list(itertools.islice(inputs, start, stop, step)) == expected

@pytest.mark.parametrize("inputs, start, stop, step, error", [
    ([1,2,3], -1, 1, 1, "Indices for islice() must be None or an integer: 0 <= x <= sys.maxsize."),
    ([1,2,3], 1, -1, 1, "Stop argument for islice() must be None or an integer: 0 <= x <= sys.maxsize."),
    ([1,2,3], 1, 1, -1, "Step for islice() must be a positive integer or None."),
])
def test_islice_value_error(inputs, start, stop, step, error):
    with pytest.raises(ValueError) as excinfo:
        list(itertools.islice(inputs, start, stop, step))
    assert excinfo.value.args[0] == error

@pytest.mark.parametrize("inputs, error", [
    ([1,2,3], "islice expected at least 2 arguments, got 1")
])
def test_islice_type_error_1_arg(inputs, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.islice(inputs))
    assert excinfo.value.args[0] == error

@pytest.mark.parametrize("inputs, start, stop, step, redundant, error", [
    ([1,2,3], 1, 1, 1, 1, "islice expected at most 4 arguments, got 5")
])
def test_islice_type_error_5_arg(inputs, start, stop, step, redundant, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.islice(inputs, start, stop, step, redundant))
    assert excinfo.value.args[0] == error
