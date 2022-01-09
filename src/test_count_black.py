# By Jyong-Jhih Lin
# Software Testing Project 2021 Aumumn period 2: itertools, python=3.9.7
# count(), blackbox


from itertools import count
import pytest
import sys
import decimal

# check "count()" type
def test_count_type():
    assert str(type(count())) == "<class 'itertools.count'>"


# check default value
def test_count_default():
    test = count()
    assert next(test) == 0
    assert next(test) == 1
    assert next(test) == 2


# check normal usage
def test_count_normal():
    test = count(start=0, step=1)
    assert next(test) == 0
    assert next(test) == 1
    assert next(test) == 2
    test = count(start=0, step=0)
    assert next(test) == 0
    assert next(test) == 0
    assert next(test) == 0
    test = count(start=0, step=2)
    assert next(test) == 0
    assert next(test) == 2
    assert next(test) == 4
    test = count(start=0, step=3)
    assert next(test) == 0
    assert next(test) == 3
    assert next(test) == 6


# check mixed type
def test_count_mixed_type():
    test = count(start=0, step=1)
    assert next(test) == 0
    assert next(test) == 1
    assert next(test) == 2
    test = count(start=0.1, step=1)
    assert next(test) == 0.1
    assert next(test) == 0.1+1
    assert next(test) == 0.1+1+1
    test = count(start=0, step=0.1)
    assert next(test) == 0
    assert next(test) == 0+0.1
    assert next(test) == 0+0.1+0.1
    test = count(start=0.1, step=1.1)
    assert next(test) == 0.1
    assert next(test) == 0.1+1.1
    assert next(test) == 0.1+1.1+1.1
    #####
    test = count(start=0+0j, step=1)
    assert next(test) == 0+0j
    assert next(test) == 1+0j
    assert next(test) == 2+0j
    test = count(start=0+0j, step=1.1)
    assert next(test) == 0+0j
    assert next(test) == 0+0j+1.1
    assert next(test) == 0+0j+1.1+1.1
    test = count(start=0+0j, step=1.1+1.1j)
    assert next(test) == 0+0j
    assert next(test) == 1.1+1.1j
    assert next(test) == 1.1+1.1j+1.1+1.1j
    #####
    test = count(start=False, step=1)
    assert next(test) == 0
    assert next(test) == 1
    assert next(test) == 2
    test = count(start=True, step=1)
    assert next(test) == 1
    assert next(test) == 2
    assert next(test) == 3
    test = count(start=False, step=0.1)
    assert next(test) == 0
    assert next(test) == 0+0.1
    assert next(test) == 0+0.1+0.1
    test = count(start=True, step=1.1)
    assert next(test) == 1
    assert next(test) == 1+1.1
    assert next(test) == 1+1.1+1.1
    test = count(start=False, step=True)
    assert next(test) == 0
    assert next(test) == 1
    assert next(test) == 2
    test = count(start=True, step=True)
    assert next(test) == 1
    assert next(test) == 2
    assert next(test) == 3
    test = count(start=False, step=False)
    assert next(test) == 0
    assert next(test) == 0
    assert next(test) == 0
    test = count(start=True, step=False)
    assert next(test) == 1
    assert next(test) == 1
    assert next(test) == 1


# check overflow, underflow
def test_count_overflowl():
    test = count(start=sys.float_info.max, step=sys.float_info.max)
    assert next(test) == sys.float_info.max
    assert next(test) == float('inf')
    assert next(test) == float('inf')
    test = count(start=-sys.float_info.max, step=-sys.float_info.max)
    assert next(test) == -sys.float_info.max
    assert next(test) == float('-inf')
    assert next(test) == float('-inf')


# check error
@pytest.mark.parametrize("input, input2, exception_message", [
    (1, "1", "a number is required"),
    ("1", 1, "a number is required"),
    ("1", "1", "a number is required"),
    (1, (1,1), "a number is required"),
    ((1,1), 1, "a number is required"),
    ((1,1), (1,1), "a number is required"),
    (1, {1,1}, "a number is required"),
    ({1,1}, {1,1}, "a number is required"),
    ({1,1}, 1, "a number is required"),
    (1, {"a":"b"}, "a number is required"),
    ({"a":"b"}, {"a":"b"}, "a number is required"),
    ({"a":"b"}, 1, "a number is required")
])
def test_count_error(input, input2, exception_message):
    with pytest.raises(TypeError) as excinfo:
        test = count(start=input, step=input2)
    assert excinfo.value.args[0] == exception_message