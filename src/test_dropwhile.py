import itertools
import pytest

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 1, [], []),
    (lambda x : x < 6, [0,1,2,3,4,5], []),
    (lambda x : x > -6, [0,-1,-2,-3,-4,-5], []),
    (lambda x : x == 10, [10,10,10], []),
    (lambda x : x != 10, [34,-68,97.215,"10"], [])
])
def test_dropwhile_null(predicate, inputs, expected):
    result = list(itertools.dropwhile(predicate, inputs))
    assert result == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 1, [0,1,2,3], [1,2,3]),
    (lambda x : x < -1, [-3,-2,-1,0], [-1,0]),
    (lambda x : x != 0, [-2,-1,0,1,2], [0,1,2]),
    (lambda x : x < 5, [2,1,9,10,6,5,3,8,7,4,0], [9,10,6,5,3,8,7,4,0]),
    (lambda x : x < 0, [-1,-2,-3,-4,-5,1,2,3,4,5], [1,2,3,4,5]),
    (lambda x : x < 0, [1,2,3,4,5,-1,-2,-3,-4,-5], [1,2,3,4,5,-1,-2,-3,-4,-5])
])
def test_dropwhile_int(predicate, inputs, expected):
    result = list(itertools.dropwhile(predicate, inputs))
    assert result == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 0.25, [0.1,1.25,2.5,3.75], [1.25,2.5,3.75]),
    (lambda x : x < -0.25, [-3.75,-2.5,-1.25,0.1], [0.1]),
    (lambda x : x != 0.25, [-2.75,-1.5,0.25,1.33,2.66], [0.25,1.33,2.66]),
    (lambda x : x < 0.5, [0.4999999999999999,0.5000000000000001],
                         [0.5000000000000001]),
    (lambda x : x < 0.5, [-1.23,-2.34,-3.45,1.23,2.34,3.45], [1.23,2.34,3.45]),
    (lambda x : x < 0.5, [1.23,2.34,3.45,-1.23,-2.34,-3.45],
                         [1.23,2.34,3.45,-1.23,-2.34,-3.45])
])
def test_dropwhile_float(predicate, inputs, expected):
    result = list(itertools.dropwhile(predicate, inputs))
    assert result == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < "c", ["a","b","c","d"], ["c","d"]),
    (lambda x : x < "w", ["h","e","l","l","o"," ","w","o","r","l","d"],
                         ["w","o","r","l","d"]),
    (lambda x : x < "c", ["apple","banana","cherry","date"], ["cherry","date"]),
    (lambda x : x < "sentence", ["here","is","one","sentence"], ["sentence"])
])
def test_dropwhile_char(predicate, inputs, expected):
    result = list(itertools.dropwhile(predicate, inputs))
    assert result == expected

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < [1], [[0,1], [2,3]], [[2,3]]),
    (lambda x : x < ["b"], [["a","b"], ["c","d"]], [["c","d"]]),
    (lambda x : x < ["one"], [["here","is"], ["one","sentence"]],
                    [["one","sentence"]]),
    (lambda x : x < [[1]], [[[0,1], [2,3]], [[4,5], [6,7]]], [[[4,5], [6,7]]])
])
def test_dropwhile_list(predicate, inputs, expected):
    result = list(itertools.dropwhile(predicate, inputs))
    assert result == expected

'''
@pytest.mark.parametrize("predicate, inputs, error", [
    (lambda x : x < 1, [[0,1]], "'<' not supported between instances of 'list' and 'int'")
])
def test_dropwhile_error(predicate, inputs, error):
    with pytest.raises(TypeError) as excinfo:
        itertools.dropwhile(predicate, inputs)
        exception_msg = excinfo.value.args[0]
        assert exception_msg == error
'''