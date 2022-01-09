import itertools
import pytest

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 1, [], []),          # T1 covers prime path [1,2,7]
    (lambda x : x < 1, [1], [1]),        # T2 covers prime path [1,2,3,4,5,7]
    (lambda x : x < 1, [0,0], []),       # T3 covers prime paths [2,3,2], [3,2,3] and [3,2,7]
    (lambda x : x < 1, [1,1,1], [1,1,1]) # T4 covers prime paths [5,6,5], [6,5,6], [6,5,7] and [1,2,3,4,5,6]
])
def test_dropwhile_white_box(predicate, inputs, expected):
    assert list(itertools.dropwhile(predicate, inputs)) == expected