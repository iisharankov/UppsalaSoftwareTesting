import types
import itertools
import pytest
import inspect
import numpy as np


@pytest.mark.parametrize("inputs, expected", [
    ("A", [('A',) ]),
    (("A"), [('A',) ]),
    (["A"], [('A',) ]),
    ("A1", [('A', '1'), ('1', 'A')]),
    ("1a", [('1', 'a'), ('a', '1')]),
    ("B", [('B',), ]),
    ("AB", [('A', 'B'), ('B', 'A')]),
    ("BA", [('B', 'A'), ('A', 'B')]),
    ("ABC", [('A', 'B', 'C'),  ('A', 'C', 'B'),  ('B', 'A', 'C'),
             ('B', 'C', 'A'),  ('C', 'A', 'B'),  ('C', 'B', 'A')] ),
    (range(3), [(0, 1, 2), (0, 2, 1), (1, 0, 2),
                (1, 2, 0), (2, 0, 1), (2, 1, 0)]),
])
def test_permutations_basic_case(inputs, expected):
    output = list(itertools.permutations(inputs))
    assert output == expected



# Check that any input with repeat=0 returns [()]
@pytest.mark.parametrize("inputs", [
    "A", ["A"],  ["B"],  ["AB"], ["BA"], ["ABC"],  "ABC",  ("ABC"),
    ["AB", ""], ["AB", "x"], ["AB", "xy"], ["AB", "x"]

])
def test_permutations_basic_case_with_0_repeats(inputs):
    output = list(itertools.permutations(inputs, r=0))
    assert output == [()]  # Expected output is empty list

# Check that random examples are all valid instances
@pytest.mark.parametrize("inputs", [
    "A", ["A"], ["ABC"], ["AB", "x"], ("ERFe")
])
def test_permutations_valid_instance(inputs):
    output = itertools.permutations(inputs)
    assert isinstance(output, itertools.permutations)

# Check that Type Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs, expected", [
    ([23], [(23,)]),
    ([1.35], [(1.35,)]),
    ((23, 23), [(23, 23), (23, 23)]),
    ((23, 23.5), [(23, 23.5), (23.5, 23)]),
    ((2.5, 1.543), [(2.5, 1.543), (1.543, 2.5)]),
])
def test_permutations_with_numbers(inputs, expected):
    output = list(itertools.permutations(inputs))
    assert output == expected


# Check that Type Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs, expected", [
    ([2.5, 're'], [(2.5, 're'), ('re', 2.5)]),
    ([12, 're'], [(12, 're'), ('re', 12)]),
    ([5, 'r'], [(5, 'r'), ('r', 5)]),
    ([[34, 2], 're'], [([34, 2], 're'), ('re', [34, 2])]),
    # Warning, these get ugly quick with nested lists
    ([(34, 5), [34, 5]], [((34, 5), [34, 5]), ([34, 5], (34, 5))]),
    ([(34, 5), ['A', [5]]], [((34, 5), ['A', [5]]), (['A', [5]], (34, 5))]),
    ([(34, 5), [[34, 5]]], [((34, 5), [[34, 5]]), ([[34, 5]], (34, 5))]),
    ([(34, 5), ['5', [34, 5]]], [((34, 5), ['5', [34, 5]]), (['5', [34, 5]], (34, 5))]),
    ([2.5, 're', 'T'],
     [(2.5, 're', 'T'), (2.5, 'T', 're'), ('re', 2.5, 'T'), ('re', 'T', 2.5), ('T', 2.5, 're'), ('T', 're', 2.5)]),
])
def test_permutations_with_numbers(inputs, expected):
    output = list(itertools.permutations(inputs))
    assert output == expected


# Test various different combinations of string lengths with repetition lengths, and
# just check that the shapes are valid for those sizes
@pytest.mark.parametrize("inputs, shapes", [
    ((1, 2), [(0,), (2, 1)]),
    ((1, 3), [(0,), (3, 1)]),
    ((1, 4), [(0,), (4, 1)]),
    ((1, 5), [(0,), (5, 1)]),
    ((1, 6), [(0,), (6, 1)]),
    ((1, 7), [(0,), (7, 1)]),
    ((2, 3), [(0,), (6, 2)]),
    ((2, 4), [(0,), (12, 2)]),
    ((2, 5), [(0,), (20, 2)]),
    ((2, 6), [(0,), (30, 2)]),
    ((2, 7), [(0,), (42, 2)]),
    ((3, 4), [(0,), (24, 3)]),
    ((3, 5), [(0,), (60, 3)]),
    ((3, 6), [(0,), (120, 3)]),
    ((3, 7), [(0,), (210, 3)]),
    ((4, 5), [(0,), (120, 4)]),
    ((4, 6), [(0,), (360, 4)]),
    ((4, 7), [(0,), (840, 4)]),
    ((5, 6), [(0,), (720, 5)]),
    ((5, 7), [(0,), (2520, 5)]),
    ((6, 7), [(0,), (5040, 6)]),

])
def test_shape_of_various_repetitions(inputs, shapes):
    i, j = inputs
    # Just multiply a string of len=1 to get desired length
    result1 = list(itertools.permutations("e" * i, r=j))
    result2 = list(itertools.permutations("e" * j, r=i))

    # Test both (i, j) and (j, i) combinations
    assert np.array(result1).shape == shapes[0]
    assert np.array(result2).shape == shapes[1]



# # # # # # # # Test errors # # # # # # # #


# # Check that Type Errors are triggered, and display valid message
# @pytest.mark.parametrize("inputs, error", [
#     ([23], "'int' object is not iterable"),
#     ([1.35], "'float' object is not iterable"),
#     ((23, 23), "'int' object is not iterable"),
#     ((23, 23.5), "'int' object is not iterable"),
#     ((2.5, 1.543), "'float' object is not iterable"),
# ])
# def test_permutations_type_error_exception(inputs, error):
#     with pytest.raises(TypeError) as excinfo:
#         itertools.permutations(inputs)
#
#     exception_msg = excinfo.value.args[0]
#     assert exception_msg == error


# Check that Overflow Errors are triggered, and display valid message
@pytest.mark.parametrize("inputs", [
    ["Overflow"], ["O"], [""], [2.3], [2.3, 2.5], [23, 25],
])
def test_permutations_overflow_error_exception(inputs):
    with pytest.raises(OverflowError) as excinfo:
        itertools.permutations(inputs, r=int(1e20))

    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Python int too large to convert to C ssize_t"


@pytest.mark.parametrize("inputs", [
    ["Memory"], ["M"], [""], [23], [2.33], [(2, 3)], [(23, 25)], [(2.3, 2.5)]
])
def test_permutations_memory_error_exception(inputs):
    with pytest.raises(MemoryError) as _:
        itertools.permutations(inputs, r=int(1e18))

