import types
import itertools
import pytest
import inspect
import numpy as np


# White box text tha tests all prime paths of itertools.product
@pytest.mark.parametrize("inputs, expected", [
    ("", [()]), # Tests [0, 1, 2, 3, 4, 5, 6], [6, 7 ,8, 9, 10, 6], [10, 11, 12]
    (["A"], [('A',) ]),  # Tests [2, 3, 2], [8, 9, 10, 8], [9, 10, 9]
    (["AB"], [('A',), ('B',), ]),  # Tests [12, 11, 12]
])
def test_product_basic_case(inputs, expected):
    output = list(itertools.product(*inputs))
    assert output == expected
