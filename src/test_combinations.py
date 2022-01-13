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


