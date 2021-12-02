import types
import itertools
import pytest
import inspect



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


@pytest.mark.parametrize("inputs", [
    "A", ["A"],  ["B"],  ["AB"], ["BA"], ["AB", ""],  ["AB", "x"],  ["AB", "xy"],  ["AB", "x"]
])
def test_product_basic_case_with_0_repeats(inputs):
    output = list(itertools.product(*inputs, repeat=0))  # the * extracts a list of inputs to individual inputs
    assert output == [()]  # Expected output is empty list


@pytest.mark.parametrize("inputs", [
    "A", ["A"], ["ABC"], ["AB", "x"]
])
def test_product_valid_instance(inputs):
    output = itertools.product(*inputs)  # the * extracts a list of inputs to individual inputs
    assert isinstance(output, itertools.product)


@pytest.mark.parametrize("inputs, error", [
    ([23], "'int' object is not iterable"),
    ([1.35], "'float' object is not iterable"),
    ((23, 23), "'int' object is not iterable"),
    ((23, 23.5), "'int' object is not iterable"),
    ((2.5, 1.543), "'float' object is not iterable"),
])
def test_product_type_error_exception(inputs, error):
    with pytest.raises(TypeError) as excinfo:
        itertools.product(*inputs)  # the * extracts a list of inputs to individual inputs
    exception_msg = excinfo.value.args[0]
    assert exception_msg == error

