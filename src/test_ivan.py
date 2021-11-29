import types
import itertools
import pytest
import inspect



@pytest.mark.parametrize("inputs, expected", [
    ("A", [('A',),]),
    (["A"], [('A',),]),  # Should be same as above since inputs is extracted
    (["B"], [('B',),]),
    (["AB"], [('A',), ('B',)]),
    (["BA"], [('B',), ('A',)]),
    (["AB", ""], []),
    (["AB", "x"], [("A", "x"), ("B", "x")]),
    (["AB", "xy"], [('A', 'x'), ('A', 'y'), ('B', 'x'), ('B', 'y')]),
    # (["AB", "x"], [('Ax', 'Bx')])
])
def test_product_basic_case(inputs, expected):
    output = list(itertools.product(*inputs))  # the * extracts a list of inputs to individual inputs
    assert output == expected


@pytest.mark.parametrize("inputs", [
    "A", ["A"],  ["B"],  ["AB"], ["BA"], ["AB", ""],  ["AB", "x"],  ["AB", "xy"],  ["AB", "x"]
])
def test_product_basic_case_with_0_repeats(inputs):
    print(inputs)
    output = list(itertools.product(*inputs, repeat=0))  # the * extracts a list of inputs to individual inputs
    assert output == [()]  # Expected output is empty list


@pytest.mark.parametrize("inputs", [
    "A", ["A"], ["ABC"], ["AB", "x"]
])
def test_product_valid_instance(inputs):
    output = itertools.product(*inputs)  # the * extracts a list of inputs to individual inputs
    assert isinstance(output, itertools.product)