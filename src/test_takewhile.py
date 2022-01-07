import itertools
import pytest

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x == x, [], []),
    (lambda x : x == x, [-3,-2,-1,0,1,2,3], [-3,-2,-1,0,1,2,3]),
    (lambda x : x < 6, [1,2,3,4,5], [1,2,3,4,5]),
    (lambda x : x > 6, [1,2,3,4,5], []),
    (lambda x : x % 3, [1,2,3,4,5], [1,2]),
    (lambda x : x == 10, [10,10.00000,-5+15], [10,10,10]),
    (lambda x : x != 10, [34,-68,97.215,"10"], [34,-68,97.215,"10"])
])
def test_takewhile_operators(predicate, inputs, expected):
    assert list(itertools.takewhile(predicate, inputs)) == expected
    
# proceeding with "<" as default predicate operator

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 10, [0,10,20,30], [0]),
    (lambda x : x < -10, [-30,-20,-10,0], [-30,-20]),
    (lambda x : x < 5, [2,1,9,10,6,5,3,8,7,4,0], [2,1]),
    (lambda x : x < 0, [-1,-2,-3,-4,-5,1,2,3,4,5], [-1,-2,-3,-4,-5]),
    (lambda x : x < 0, [1,2,3,4,5,-1,-2,-3,-4,-5], [])
])
def test_takewhile_int(predicate, inputs, expected):
    assert list(itertools.takewhile(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 0.25, [0.1,1.25,2.666,3.75], [0.1]),
    (lambda x : x < -0.25, [-3.75,-2.666,-1.25,0.1], [-3.75,-2.666,-1.25]),
    (lambda x : x < 0.5, [0.4999999999999999,0.5000000000000001],
                         [0.4999999999999999]),
    (lambda x : x < 0.5, [-1.23,-2.34,-3.45,1.23,2.34,3.45], [-1.23,-2.34,-3.45]),
    (lambda x : x < 0.5, [1.23,2.34,3.45,-1.23,-2.34,-3.45], [])
])
def test_takewhile_float(predicate, inputs, expected):
    assert list(itertools.takewhile(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < "c", ["a","b","c","d","c","b","a"], ["a","b"]),
    (lambda x : x < "w", ["h","e","l","l","o"," ","w","o","r","l","d"],
                         ["h","e","l","l","o"," "]),
    (lambda x : x < "c", ["apple","banana","cherry","date"], ["apple","banana"]),
    (lambda x : x < "sentence", ["here","is","one","sentence"], ["here","is","one"])
])
def test_takewhile_char(predicate, inputs, expected):
    assert list(itertools.takewhile(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < [1], [[0,1], [2,3], [-4,-5], [6,7]], [[0,1]]),
    (lambda x : x < ["b"], [["a","b"], ["c","d"]], [["a","b"]]),
    (lambda x : x < ["one"], [["here","is"], ["one","sentence"]],
                    [["here","is"]]),
    (lambda x : x < [[1]], [[[0,1], [2,3]], [[4,5], [6,7]]], [[[0,1], [2,3]]])
])
def test_takewhile_list(predicate, inputs, expected):
    assert list(itertools.takewhile(predicate, inputs)) == expected

@pytest.mark.parametrize("predicate, inputs, error", [
    (lambda x : x < 1, [[0,1]], "'<' not supported between instances of 'list' and 'int'"),
    (lambda x : x < "a", [0,1], "'<' not supported between instances of 'int' and 'str'"),
    (lambda x : x % 1, ["a","b"], "not all arguments converted during string formatting")
])
def test_takewhile_type_error(predicate, inputs, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.takewhile(predicate, inputs))
    assert excinfo.value.args[0] == error

@pytest.mark.parametrize("predicate, error", [
    (lambda x : x < 1, "takewhile expected 2 arguments, got 1")
])
def test_takewhile_type_error_1_arg(predicate, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.takewhile(predicate))
    assert excinfo.value.args[0] == error

@pytest.mark.parametrize("predicate, inputs, redundant, error", [
    (lambda x : x < 1, [0,1], 1, "takewhile expected 2 arguments, got 3")
])
def test_takewhile_type_error_3_arg(predicate, inputs, redundant, error):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.takewhile(predicate, inputs, redundant))
    assert excinfo.value.args[0] == error
