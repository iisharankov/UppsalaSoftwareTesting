import itertools as itools
import math
import pytest as pytest

# For itertools.compress
# Testing Lists, Tuples, Sets, Dictionaries each partitioned based on the values the items they hold


def generate_selector_first_item(length_of_list):
    selector = [0] * length_of_list
    selector[0] = 1
    return selector


def generate_selector_last_item(length_of_list):
    selector = [0] * length_of_list
    selector[length_of_list-1] = 1
    return selector


# Testing compress
@pytest.mark.parametrize("compressible", [
    # Lists & primitive type cases
    ([1, 2]),
    ([-1, 1]),
    ([-1, -1]),
    ([1, 3, 5, 7, 9]),
    ([math.inf, -math.inf]),
    ([math.nan, math.nan]),
    ([pow(2, 30), pow(2, 31)]),
    ([math.pi, math.e, math.tau]),
    ("ABC", "DEF"),
    ([False], [True]),
    # Tuples
    ((1, 2),
    # Sets
    ({1, 2}),
    # Dictionaries
    ({"first": 0}, {"second": 1}),
    # Combination
    ((1, 2), {3, 4}), [1, 2, 3, 4], ((1, 2), {3, 4})),
    ("ABC", {3, 4}), ["A", "B", "C", 3, 4], ("ABC", {3, 4}),
    ("012", {True, math.pi}), ["0", "1", "2", True, math.pi], ("012", {True, math.pi})
])
def test_compress(compressible):
    output_compress_first = list(itools.compress(compressible, generate_selector_first_item(len(compressible))))
    output_compress_last = list(itools.compress(compressible, generate_selector_last_item(len(compressible))))
    assert output_compress_first == [compressible[0]]
    assert output_compress_last == [compressible[len(compressible)-1]]



