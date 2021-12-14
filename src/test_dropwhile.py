import itertools
import pytest

@pytest.mark.parametrize("predicate, inputs, expected", [
    (lambda x : x < 5, [1,2,3,4,5,6,7], [5,6,7])])
def test_dropwhile(predicate, inputs, expected):
    result = list(itertools.dropwhile(predicate, inputs))
    assert result == expected
