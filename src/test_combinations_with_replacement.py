import types
import itertools
import pytest
import inspect

import numpy as np


@pytest.mark.parametrize("inputs, repetition, expected", [
    ("A", 1, [('A',)]),
    ("A", 2, [('A', 'A')]),
    ("A", 3, [('A', 'A', 'A')]),
    ("A", 4, [('A', 'A', 'A', 'A')]),
    ("AB", 1, [('A',), ('B',)]),
    ("AB", 2, [('A', 'A'), ('A', 'B'), ('B', 'B')]),
    ("AB", 3, [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'B', 'B'), ('B', 'B', 'B')]),
    ("AB", 4,
     [('A', 'A', 'A', 'A'), ('A', 'A', 'A', 'B'), ('A', 'A', 'B', 'B'), ('A', 'B', 'B', 'B'), ('B', 'B', 'B', 'B')]),
    ("ABC", 1, [('A',), ('B',), ('C',)]),
    ("ABC", 2, [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]),
    ("ABC", 3, [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'B', 'B'), ('A', 'B', 'C'), ('A', 'C', 'C'),
                ('B', 'B', 'B'), ('B', 'B', 'C'), ('B', 'C', 'C'), ('C', 'C', 'C')]),
    ("ABC", 4,
     [('A', 'A', 'A', 'A'), ('A', 'A', 'A', 'B'), ('A', 'A', 'A', 'C'), ('A', 'A', 'B', 'B'), ('A', 'A', 'B', 'C'),
      ('A', 'A', 'C', 'C'), ('A', 'B', 'B', 'B'), ('A', 'B', 'B', 'C'), ('A', 'B', 'C', 'C'), ('A', 'C', 'C', 'C'),
      ('B', 'B', 'B', 'B'), ('B', 'B', 'B', 'C'), ('B', 'B', 'C', 'C'), ('B', 'C', 'C', 'C'), ('C', 'C', 'C', 'C')]),
    ("ABCD", 1, [('A',), ('B',), ('C',), ('D',)]),
    ("ABCD", 2,
     [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'C'), ('C', 'D'),
      ('D', 'D')]),
    ("ABCD", 3, [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'), ('A', 'A', 'D'), ('A', 'B', 'B'), ('A', 'B', 'C'),
                 ('A', 'B', 'D'), ('A', 'C', 'C'), ('A', 'C', 'D'), ('A', 'D', 'D'), ('B', 'B', 'B'), ('B', 'B', 'C'),
                 ('B', 'B', 'D'), ('B', 'C', 'C'), ('B', 'C', 'D'), ('B', 'D', 'D'), ('C', 'C', 'C'), ('C', 'C', 'D'),
                 ('C', 'D', 'D'), ('D', 'D', 'D')]),
])
def test_combinations_with_replacement_general(inputs, repetition, expected):
    output = list(itertools.combinations_with_replacement(inputs, r=repetition))
    assert output == expected


@pytest.mark.parametrize("range_length, repetition, expected", [
    (1, 1, [(0,)]),
    (1, 2, [(0, 0)]),
    (1, 3, [(0, 0, 0)]),
    (1, 4, [(0, 0, 0, 0)]),
    (2, 1, [(0,), (1,)]),
    (2, 2, [(0, 0), (0, 1), (1, 1)]),
    (2, 3, [(0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)]),
    (2, 4, [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 1), (0, 1, 1, 1), (1, 1, 1, 1)]),
    (3, 1, [(0,), (1,), (2,)]),
    (3, 2, [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]),
    (3, 3, [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 1), (0, 1, 2),
            (0, 2, 2), (1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]),
    (3, 4, [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 0, 2), (0, 0, 1, 1),
            (0, 0, 1, 2), (0, 0, 2, 2), (0, 1, 1, 1), (0, 1, 1, 2),
            (0, 1, 2, 2), (0, 2, 2, 2), (1, 1, 1, 1), (1, 1, 1, 2),
            (1, 1, 2, 2), (1, 2, 2, 2), (2, 2, 2, 2)]),
    (4, 1, [(0,), (1,), (2,), (3,)]),
    (4, 2, [(0, 0), (0, 1), (0, 2), (0, 3), (1, 1),
            (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]),
    (4, 3, [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 0, 3), (0, 1, 1),
            (0, 1, 2), (0, 1, 3), (0, 2, 2), (0, 2, 3), (0, 3, 3),
            (1, 1, 1), (1, 1, 2), (1, 1, 3), (1, 2, 2), (1, 2, 3),
            (1, 3, 3), (2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]),
])
def test_combinations_with_replacement_on_range(range_length, repetition, expected):
    output = list(itertools.combinations_with_replacement(list(range(range_length)), r=repetition))
    assert output == expected

@pytest.mark.parametrize("inputs, repetition, expected", [
    ([22], 1, [(22,)]),
    ([61], 2, [(61, 61)]),
    ([58], 3, [(58, 58, 58)]),
    ([73], 4, [(73, 73, 73, 73)]),
    ([36, 21], 1, [(36,), (21,)]),
    ([67, 62], 2, [(67, 67), (67, 62), (62, 62)]),
    ([8, 71], 3, [(8, 8, 8), (8, 8, 71), (8, 71, 71), (71, 71, 71)]),
    ([72, 66], 4, [(72, 72, 72, 72), (72, 72, 72, 66), (72, 72, 66, 66), (72, 66, 66, 66), (66, 66, 66, 66)]),
    ([60, 34, 60], 1, [(60,), (34,), (60,)]),
    ([44,  6, 49], 2, [(44, 44), (44, 6), (44, 49), (6, 6), (6, 49), (49, 49)]),
    ([3, 59, 43], 3,
     [(3, 3, 3), (3, 3, 59), (3, 3, 43), (3, 59, 59), (3, 59, 43), (3, 43, 43), (59, 59, 59), (59, 59, 43),
      (59, 43, 43), (43, 43, 43)]),
    ([36, 15, 56], 4,
     [(36, 36, 36, 36), (36, 36, 36, 15), (36, 36, 36, 56), (36, 36, 15, 15), (36, 36, 15, 56), (36, 36, 56, 56),
      (36, 15, 15, 15), (36, 15, 15, 56), (36, 15, 56, 56), (36, 56, 56, 56), (15, 15, 15, 15), (15, 15, 15, 56),
      (15, 15, 56, 56), (15, 56, 56, 56), (56, 56, 56, 56)]),
    ([22, 42, 48, 68], 1, [(22,), (42,), (48,), (68,)]),
    ([6, 28, 35, 31], 2, [(6, 6), (6, 28), (6, 35), (6, 31), (28, 28), (28, 35), (28, 31), (35, 35), (35, 31), (31, 31)]),
    ([55, 24, 64, 58], 3,
     [(55, 55, 55), (55, 55, 24), (55, 55, 64), (55, 55, 58), (55, 24, 24), (55, 24, 64), (55, 24, 58), (55, 64, 64),
      (55, 64, 58), (55, 58, 58), (24, 24, 24), (24, 24, 64), (24, 24, 58), (24, 64, 64), (24, 64, 58), (24, 58, 58),
      (64, 64, 64), (64, 64, 58), (64, 58, 58), (58, 58, 58)]),
])
def test_combinations_with_replacement_on_random_vals(inputs, repetition, expected):
    output = list(itertools.combinations_with_replacement(inputs, r=repetition))
    assert output == expected

# Check that random examples are all valid instances
@pytest.mark.parametrize("inputs", [
    "A", "ABC", "ABCDE", ["ABC"]
])
def test_combinations_with_replacement_valid_instance(inputs):
    output = itertools.combinations_with_replacement(inputs, r=1)
    assert isinstance(output, itertools.combinations_with_replacement)


##############
@pytest.mark.parametrize("inputs", [
    ["Error"], ["Test"], [""], [42], [23.54], [25, 28],
])
def test_product_overflow_error_exception(inputs):
    with pytest.raises(TypeError) as excinfo:
        itertools.combinations_with_replacement(inputs)

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "combinations_with_replacement() missing required argument 'r' (pos 2)"

# Check that Overflow Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs", [
    ["Overflow"], ["O"], [""], [2.3], [2.3, 2.5], [23, 25],
])
def test_combinations_with_replacement_overflow_error_exception(inputs):
    with pytest.raises(OverflowError) as excinfo:
        itertools.combinations_with_replacement(inputs, r=int(1e20))

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Python int too large to convert to C ssize_t"
