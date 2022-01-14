import itertools as itools
import math
import pytest as pytest

# For itertools.chain and chain.from_iterable
# Testing Lists, Tuples, Sets, Dictionaries each partitioned based on the values the items they hold
# By Onur Yuksel

# Testing chain and chain.from_iterable against data types
@pytest.mark.parametrize("chainables, expected_when_chained", [
    # Lists & primitive type cases
    (([1], [2]), [1, 2]),
    (([-1], [1]), [-1, 1]),
    (([-1], [-1]), [-1, -1]),
    (([1, 3, 5, 7, 9], [2, 4, 6, 8, 10]), [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]),
    (([math.inf], [-math.inf]), [math.inf, -math.inf]),
    (([math.nan], [math.nan]), [math.nan, math.nan]),
    (([pow(2, 30)], [pow(2, 31)]), [pow(2, 30), pow(2, 31)]),
    (([math.pi, math.e, math.tau], [math.pi, math.e, math.tau]),
     [math.pi, math.e, math.tau, math.pi, math.e, math.tau]),
    (("ABC", "DEF"), ["A", "B", "C", "D", "E", "F"]),
    (([False], [True]), [False, True]),
    # Tuples
    (((1, 2), (3, 4)), [1, 2, 3, 4]),
    # Sets
    (({1, 2}, {3, 4}), [1, 2, 3, 4]),
    # Dictionaries
    (({"first": 0}, {"second": 1}), ["first", "second"]),
    # Combination
    (((1, 2), {3, 4}), [1, 2, 3, 4]),
    (("ABC", {3, 4}), ["A", "B", "C", 3, 4]),
    (("012", {True, math.pi}), ["0", "1", "2", True, math.pi])
    # The following does not assert true : (("012", {True, False, math.pi}), ["0", "1", "2", True, False, math.pi])
    # Might have catched an error of the library
])
def test_chain_two_sets_of_vars(chainables, expected_when_chained):
    output_chain = list(itools.chain(*chainables))
    output_chain_from_iterable = list(itools.chain.from_iterable(chainables))
    assert output_chain == expected_when_chained
    assert output_chain_from_iterable == expected_when_chained


# Testing chain and chain.from_iterable against empty values
@pytest.mark.parametrize("chainables, expected", [
    (([0], []), [0]),
    (([], [1]), [1]),
    (([], []), []),
    (([""], [""]), ["", ""]),
    (((), ()), []),
    (({}, ()), []),
])
def test_chain_empty_sets(chainables, expected):
    output_chain = list(itools.chain(*chainables))
    output_chain_from_iterable = list(itools.chain.from_iterable(chainables))
    assert output_chain == expected
    assert output_chain_from_iterable == expected


