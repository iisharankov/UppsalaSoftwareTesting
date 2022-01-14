import types
import itertools
import pytest
import inspect

import numpy as np


@pytest.mark.parametrize("inputs, repetition, expected", [
    ("A", 1, [('A',)]),
    ("A", 2, []),
    ("AB", 1, [('A',), ('B',)]),
    ("AB", 2, [('A', 'B')]),
    ("ABC", 1, [('A',), ('B',), ('C',)]),
    ("ABC", 2, [('A', 'B'), ('A', 'C'), ('B', 'C')]),
    ("ABC", 3, [('A', 'B', 'C')]),
    ("ABCD", 1, [('A',), ('B',), ('C',), ('D',)]),
    ("ABCD", 2, [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'C'), ('B', 'D'), ('C', 'D')]),
    ("ABCD", 3, [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]),
    ("ABCD", 4, [('A', 'B', 'C', 'D')]),
])
def test_combinations_basic_case(inputs, repetition, expected):
    output = list(itertools.combinations(inputs, r=repetition))
    assert output == expected


@pytest.mark.parametrize("range_length, repetition, expected", [
    (1, 1, [(0,)]),
    (2, 1, [(0,), (1,)]),
    (2, 2, [(0, 1)]),
    (3, 1, [(0,), (1,), (2,)]),
    (3, 2, [(0, 1), (0, 2), (1, 2)]),
    (3, 3, [(0, 1, 2)]),
    (4, 1, [(0,), (1,), (2,), (3,)]),
    (4, 2, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]),
    (4, 3, [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]),
    (4, 4, [(0, 1, 2, 3)])
])
def test_combinations_on_range(range_length, repetition, expected):
    output = list(itertools.combinations(range(range_length), r=repetition))
    assert output == expected


# Check that random examples are all valid instances
@pytest.mark.parametrize("inputs", [
    "A", "ABC", "ABCDE", ["ABC"]
])
def test_combinations_valid_instance(inputs):
    output = itertools.combinations(inputs, r=1)
    assert isinstance(output, itertools.combinations)


# Check that Overflow Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs", [
    ["Overflow"], ["O"], [""], [2.3], [2.3, 2.5], [23, 25],
])
def test_combinations_overflow_error_exception(inputs):
    with pytest.raises(OverflowError) as excinfo:
        itertools.combinations(inputs, r=int(1e20))

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Python int too large to convert to C ssize_t"

##############33
@pytest.mark.parametrize("inputs", [
    ["Error"], ["Test"], [""], [42], [23.54], [25, 28],
])
def test_product_overflow_error_exception(inputs):
    with pytest.raises(TypeError) as excinfo:
        itertools.combinations(inputs)

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "combinations() missing required argument 'r' (pos 2)"
