import itertools    
import pytest


@pytest.mark.parametrize("input, initial, expected", [
    ([1, 2, 3], None, [1, 3, 6]), # T1
    ([], None, []), # T2
    ([2], 1, [1, 3]), # T3
    ([], 1, [1]), # T4
    ([1], None, [1]) # T5
])
def test_accumulate_white_box(input, initial, expected):
    assert list(itertools.accumulate(input, initial=initial)) == expected