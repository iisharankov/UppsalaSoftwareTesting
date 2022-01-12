import itertools as itools
import math
import pytest as pytest

# For itertools.chain White Box Testing
# By Onur Yuksel


@pytest.mark.parametrize("chainables, expected_when_chained", [
    # (1) Inner loop condition returns false while outer loop condition still return true:
    (("ABC", "EF"), ["A", "B", "C", "E", "F"]),
    # (2) Inner loop  and outer loop conditions return true together until they are false at the same time:
    (("ABC", "DEF"), ["A", "B", "C", "D", "E", "F"]),
    # (3) Inner loop condition returns true while outer loop condition returns false before, another alternative for (1)
    (("BC", "DEF"), ["B", "C", "D", "E", "F"]),
    # (4) Inner loop condition never returns true
    (("ABC", ""), ["A", "B", "C"]),
    # (5) Outer loop condition never returns true
    (("", ""), [])
])
def test_chain_white_box(chainables, expected_when_chained):
    output_chain = list(itools.chain(*chainables))
    assert output_chain == expected_when_chained
