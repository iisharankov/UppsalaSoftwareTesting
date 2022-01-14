import itertools as itools
import math
import pytest as pytest

# For itertools.zip_longest
# Testing Lists, Tuples, Sets, Dictionaries each partitioned based on the values the items they hold
# By Onur Yuksel

# Testing zip_longest
@pytest.mark.parametrize("zippable1, zippable2, expected", [
    # Lists & primitive type cases
    (([1, 2]), ([3, 4]), ([(1, 3), (2, 4)])),
    (([1, 2]), ([3]), ([(1, 3), (2, None)])),
    (([-1, -2]), ([-3]), ([(-1, -3), (-2, None)])),
    (([math.pi, -2]), ([math.tau]), ([(math.pi, math.tau), (-2, None)])),
    (([pow(2, 30), pow(2, 31)]), ([1]), ([(pow(2, 30), 1), (pow(2, 31), None)])),
    ((["ABC", "DEF"]), (["X"]), ([("ABC", "X"), ("DEF", None)])),
    (([False,  True]), ([False]), ([(False, False), (True, None)])),
    # Tuples
    ((1, 2), (2, 3), ([(1, 2), (2, 3)])),
    # Sets
    ({1, 2}, {2, 3}, ([(1, 2), (2, 3)])),
    # Dictionaries
    ({"first": 0, "second": 1}, {"third": 1}, ([("first", "third"), ("second", None)])),
    # Combination
    ((["ABC", math.pi]), {"second": 1}, ([("ABC", "second"), (math.pi, None)])),
    (([False, math.nan]), {"first": 1, "second": 0, "third": 0},
     ([(False, "first"), (math.nan, "second"), (None, "third")])),

])
def test_zip_longest(zippable1, zippable2, expected):
    output_zipped = list(itools.zip_longest(zippable1, zippable2))
    assert output_zipped == expected
