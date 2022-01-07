import itertools
import pytest

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x == x, [], []),
    (lambda x : x == x, [-3,-2,-1,0,1,2,3], []),
    (lambda x : x < 6, [1,2,3,4,5], []),
    (lambda x : x > 6, [1,2,3,4,5], [1,2,3,4,5]),
    (lambda x : x % 3, [1,2,3,4,5], [3]),
    (lambda x : x == 10, [10,10.00000,-5+15], []),
    (lambda x : x != 10, [34,-68,97.215,"10"], [])
])
def test_filterfalse_operators(predicate, inputs, expected):
    assert list(itertools.filterfalse(predicate, inputs)) == expected

# proceeding with "%" as default predicate operator

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x % 10, [0,10,20,30], [0,10,20,30]),
    (lambda x : x % -10, [-30,-20,-10,0], [-30,-20,-10,0]),
    (lambda x : x % 3, [2,1,9,10,6,5,3,8,7,4,0], [9,6,3,0]),
    (lambda x : x % 2, [-1,-2,-3,-4,-5,1,2,3,4,5], [-2,-4,2,4]),
    (lambda x : x % 2, [1,2,3,4,5,-1,-2,-3,-4,-5], [2,4,-2,-4])
])
def test_filterfalse_int(predicate, inputs, expected):
    assert list(itertools.filterfalse(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x % 0.25, [0.1,1.25,2.666,3.75], [1.25,3.75]),
    (lambda x : x % -0.25, [-3.75,-2.666,-1.25,0.1], [-3.75,-1.25]),
    (lambda x : x % 0.5, [0.4999999999999999,0.5000000000000001], []),
    (lambda x : x % 0.5, [-1.23,-2.34,-3.45,1.23,2.34,3.45], []),
    (lambda x : x % 0.5, [1.23,2.34,3.45,-1.23,-2.34,-3.45], [])
])
def test_filterfalse_float(predicate, inputs, expected):
    assert list(itertools.filterfalse(predicate, inputs)) == expected

# proceeding with "<" as default predicate operator

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < "c", ["a","b","c","d","c","b","a"], ["c","d","c"]),
    (lambda x : x < "w", ["h","e","l","l","o"," ","w","o","r","l","d"], ["w"]),
    (lambda x : x < "c", ["apple","banana","cherry","date"], ["cherry","date"]),
    (lambda x : x < "sentence", ["here","is","one","sentence"], ["sentence"])
])
def test_filterfalse_char(predicate, inputs, expected):
    assert list(itertools.filterfalse(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < [1], [[0,1], [2,3], [-4,-5], [6,7]], [[2,3], [6,7]]),
    (lambda x : x < ["b"], [["a","b"], ["c","d"]], [["c","d"]]),
    (lambda x : x < ["one"], [["here","is"], ["one","sentence"]],
                    [["one","sentence"]]),
    (lambda x : x < [[1]], [[[0,1], [2,3]], [[4,5], [6,7]]], [[[4,5], [6,7]]])
])
def test_filterfalse_list(predicate, inputs, expected):
    assert list(itertools.filterfalse(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, error", [
    (lambda x : x < 1, [[0,1]], "'<' not supported between instances of 'list' and 'int'"),
    (lambda x : x < "a", [0,1], "'<' not supported between instances of 'int' and 'str'"),
    (lambda x : x % 1, ["a","b"], "not all arguments converted during string formatting")
])
def test_filterfalse_type_error(predicate, inputs, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.filterfalse(predicate, inputs))
    assert excinfo.value.args[0] == error

@pytest.mark.parametrize("predicate, error", [
    (lambda x : x < 1, "filterfalse expected 2 arguments, got 1")
])
def test_filterfalse_type_error_1_arg(predicate, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.filterfalse(predicate))
    assert excinfo.value.args[0] == error

@pytest.mark.parametrize("predicate, inputs, redundant, error", [
    (lambda x : x < 1, [0,1], 1, "filterfalse expected 2 arguments, got 3")
])
def test_filterfalse_type_error_3_arg(predicate, inputs, redundant, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.filterfalse(predicate, inputs, redundant))
    assert excinfo.value.args[0] == error
