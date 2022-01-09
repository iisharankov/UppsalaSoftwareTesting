# By Jyong-Jhih Lin
# Software Testing Project 2021 Aumumn period 2: itertools, python=3.9.7
# repeat(), blackbox


from itertools import repeat
import pytest
import sys
import decimal

# check "repeat()" type
def test_repeat_type():
    assert str(type(repeat('a',1))) == "<class 'itertools.repeat'>"


# check default value
def test_repeat_default():
    with pytest.raises(TypeError) as excinfo:
        test = repeat()
    assert excinfo.value.args[0] == "repeat() missing required argument 'object' (pos 1)"


# check normal usage
@pytest.mark.parametrize("input, input2, exception_message", [
    (1, 2, [1,1]),
    (1, 0, []),
    (1, -1, []),
    ("a", 2, ["a","a"]),
    (1.1, 2, [1.1,1.1]),
    (0+1j, 2, [0+1j,0+1j]),
    ([1], 2, [[1],[1]]),
    ((1), 2, [(1),(1)]),
    ({1}, 2, [{1},{1}]),
    ({0:1}, 2, [{0:1},{0:1}])
])
def test_repeat_normal(input, input2, exception_message):
    assert list(repeat(input, input2)) == exception_message


# check error
@pytest.mark.parametrize("input, input2, exception_message", [
    (1, "1", "'str' object cannot be interpreted as an integer"),
    (1, 1.1, "integer argument expected, got float"),
    (1, (1,1), "'tuple' object cannot be interpreted as an integer"),
    (1, {1,1}, "'set' object cannot be interpreted as an integer"),
    (1, 1+1j, "'complex' object cannot be interpreted as an integer"),
    (1, {"a":"b"}, "'dict' object cannot be interpreted as an integer")
])
def test_repeat_default(input, input2, exception_message):
    with pytest.raises(TypeError) as excinfo:
        test = repeat(input, input2)
    assert excinfo.value.args[0] == exception_message