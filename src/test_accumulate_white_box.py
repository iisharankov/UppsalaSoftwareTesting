import itertools    
import pytest


@pytest.mark.parametrize("input, initial, expected", [
    ([1, 2, 3], None, [1, 3, 6]), # T1 covers prime paths [5, 6, 5], [6, 5, 6], [6, 5, 7] and [0, 1, 3, 4, 5, 6]
    ([], None, []),               # T2 covers prime path [0, 1, 2, 7]
    ([2], 1, [1, 3]),             # T3 covers prime path [0, 4, 5, 6]
    ([], 1, [1]),                 # T4 covers prime path [0, 4, 5, 7]
    ([1], None, [1])              # T5 covers prime path [0, 1, 3, 4, 5, 7]
])
def test_accumulate_white_box(input, initial, expected):
    assert list(itertools.accumulate(input, initial=initial)) == expected