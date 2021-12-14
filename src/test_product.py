import types
import itertools
import pytest
import inspect
import numpy as np


# Basic tests of the function
@pytest.mark.parametrize("inputs, expected", [
    ("A", [('A',) ]),
    (["A"], [('A',) ]),  # Should be same as above since inputs is extracted
    (["B"], [('B',), ]),
    (["AB"], [('A',), ('B',)]),
    (["BA"], [('B',), ('A',)]),
    (["AB", ""], []),
    (["AB", "x"], [("A", "x"), ("B", "x")]),
    (["AB", "xy"], [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')]),
])
def test_product_basic_case(inputs, expected):
    output = list(itertools.product(*inputs))  # the * extracts a list of inputs to individual inputs
    assert output == expected


# Check that any input with repeat=0 returns [()]
@pytest.mark.parametrize("inputs", [
    "A", ["A"],  ["B"],  ["AB"], ["BA"], ["AB", ""],  ["AB", "x"],  ["AB", "xy"],  ["AB", "x"]
])
def test_product_basic_case_with_0_repeats(inputs):
    output = list(itertools.product(*inputs, repeat=0))
    assert output == [()]  # Expected output is empty list


# Check that random examples are all valid instances
@pytest.mark.parametrize("inputs", [
    "A", ["A"], ["ABC"], ["AB", "x"]
])
def test_product_valid_instance(inputs):
    output = itertools.product(*inputs)
    assert isinstance(output, itertools.product)


# Test various different combinations of string lengths with repetition lengths, and
# just check that the shapes are valid for those sizes
@pytest.mark.parametrize("inputs, shapes", [
    ((1, 2), [(1, 2), (2, 1)]),
    ((1, 3), [(1, 3), (3, 1)]),
    ((1, 4), [(1, 4), (4, 1)]),
    ((1, 5), [(1, 5), (5, 1)]),
    ((1, 6), [(1, 6), (6, 1)]),
    ((2, 3), [(8, 3), (9, 2)]),
    ((2, 4), [(16, 4), (16, 2)]),
    ((2, 5), [(32, 5), (25, 2)]),
    ((2, 6), [(64, 6), (36, 2)]),
    ((3, 4), [(81, 4), (64, 3)]),
    ((3, 5), [(243, 5), (125, 3)]),
    ((3, 6), [(729, 6), (216, 3)]),
    ((4, 5), [(1024, 5), (625, 4)]),
    ((4, 6), [(4096, 6), (1296, 4)]),
    ((5, 6), [(15625, 6), (7776, 5)]),
])
def test_shape_of_various_repetitions(inputs, shapes):
    i, j = inputs
    # Just multiply a string of len=1 to get desired length
    result1 = list(itertools.product("e" * i, repeat=j))
    result2 = list(itertools.product("e" * j, repeat=i))

    # Test both (i, j) and (j, i) combinations
    assert np.array(result1).shape == shapes[0]
    assert np.array(result2).shape == shapes[1]


# # # # # # # # Test errors # # # # # # # #


# Check that Type Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs, error", [
    ([23], "'int' object is not iterable"),
    ([1.35], "'float' object is not iterable"),
    ((23, 23), "'int' object is not iterable"),
    ((23, 23.5), "'int' object is not iterable"),
    ((2.5, 1.543), "'float' object is not iterable"),
])
def test_product_type_error_exception(inputs, error):
    with pytest.raises(TypeError) as excinfo:
        itertools.product(*inputs)

    exception_msg = excinfo.value.args[0]
    assert exception_msg == error


# Check that Overflow Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs", [
    ["Overflow"], ["O"], [""], [2.3], [2.3, 2.5], [23, 25],
])
def test_product_overflow_error_exception(inputs):
    with pytest.raises(OverflowError) as excinfo:
        itertools.product(*inputs, repeat=int(1e20))

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Python int too large to convert to C ssize_t"


@pytest.mark.parametrize("inputs", [
    ["Memory"], ["M"], [""], [23], [2.33], [(2, 3)], [(23, 25)], [(2.3, 2.5)]
])
def test_product_memory_error_exception(inputs):
    with pytest.raises(MemoryError) as _:
        itertools.product(*inputs, repeat=int(1e18))


