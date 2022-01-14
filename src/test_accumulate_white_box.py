import itertools    
import pytest


@pytest.mark.parametrize("input, initial, expected", [
    ([20, 30], None, [20, 50]), # T1 covers all nodes ([0], [1], [2], [3], [4], [5] and [6])
])
def test_accumulate_white_box_node_coverage(input, initial, expected):
    assert list(itertools.accumulate(input, initial=initial)) == expected


@pytest.mark.parametrize("input, initial, expected", [
    ([20, 30], None, [20, 50]), # T1 covers edges [0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [4, 6] and [5, 4]
    ([], 10, [10]),             # T2 covers edges [0, 3], [3, 4] and [4, 6]
    ([], None, [])              # T3 covers edges [0, 1] and [1, 6]
])
def test_accumulate_white_box_edge_coverage(input, initial, expected):
    assert list(itertools.accumulate(input, initial=initial)) == expected


@pytest.mark.parametrize("input, initial, expected", [
    ([10, 20, 30], None, [10, 30, 60]), # T1 covers prime paths [4, 5, 4], [5, 4, 5], [5, 4, 6] and [0, 1, 2, 3, 4, 5]
    ([], None, []),                     # T2 covers prime path [0, 1, 6]
    ([20], 10, [10, 30]),               # T3 covers prime path [0, 3, 4, 5]
    ([], 10, [10]),                     # T4 covers prime path [0, 3, 4, 6]
    ([10], None, [10])                  # T5 covers prime path [0, 1, 2, 3, 4, 6]
])
def test_accumulate_white_box_prime_paths(input, initial, expected):
    assert list(itertools.accumulate(input, initial=initial)) == expected