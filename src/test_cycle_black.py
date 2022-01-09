# By Jyong-Jhih Lin
# Software Testing Project 2021 Aumumn period 2: itertools, python=3.9.7
# cycle(), blackbox


from itertools import cycle
import pytest
import sys
import decimal

# check "cycle()" type
def test_cycle_type():
    assert str(type(cycle('a'))) == "<class 'itertools.cycle'>"


# check default value
@pytest.mark.parametrize("input, exception_message", [
    (1, "'int' object is not iterable"),
])
def test_cycle_default(input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        test = cycle(input)
    assert excinfo.value.args[0] == exception_message

def test_cycle_default2():
    with pytest.raises(TypeError) as excinfo:
        test = cycle()
    assert excinfo.value.args[0] == "cycle expected 1 argument, got 0"


# check lists
@pytest.mark.parametrize("input, exception_message", [
    (["apple", "banana", "cherry"], ["apple", "banana", "cherry"]),
    (["apple", "banana", ["a","b","c"]], ["apple", "banana", ["a","b","c"]]),
    ([1, 1.1, 0+1j, min], [1, 1.1, 0+1j, min])
])
def test_cycle_lists(input, exception_message):
    elen = len(exception_message)
    test = cycle(input)
    for i in range(0, elen*2-1):
        assert next(test) == exception_message[i % elen]


# check tuples
@pytest.mark.parametrize("input, exception_message", [
    (("apple", "banana", "cherry"), ("apple", "banana", "cherry")),
    (("apple", "banana", ["a","b","c"]), ("apple", "banana", ["a","b","c"])),
    ((1, 1.1, 0+1j, min), (1, 1.1, 0+1j, min))
])
def test_cycle_tuples(input, exception_message):
    elen = len(exception_message)
    test = cycle(input)
    for i in range(0, elen*2-1):
        assert next(test) == exception_message[i % elen]


# check sets
# I think using cycle on sets is illogical
@pytest.mark.parametrize("input, exception_message", [
    ({"apple", "banana", "cherry"}, {"apple", "banana", "cherry"}),
    ({"apple", "banana", ("a","b","c")}, {"apple", "banana", ("a","b","c")}),
    ({1, 1.1, 0+1j, min}, {1, 1.1, 0+1j, min})
])
def test_cycle_sets(input, exception_message):
    elen = len(exception_message)
    em = list(exception_message)
    test = cycle(input)
    for i in range(0, elen*2-1):
        assert next(test) == em[i % elen]


# check dictionaries
@pytest.mark.parametrize("input, exception_message", [
    ({0:"apple", '1s':"banana", (3.3):"cherry"}, [0,'1s',(3.3)]),
])
def test_cycle_dictionaries(input, exception_message):
    elen = len(exception_message)
    test = cycle(input)
    for i in range(0, elen*2-1):
        assert next(test) == exception_message[i % elen]