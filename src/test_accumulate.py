import itertools
import operator
import pytest


@pytest.mark.parametrize("input, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2], [1, 3]),
    ([1, 2, 3], [1, 3, 6]),
])
def test_accumulate_default_behaviour_basic_case(input, expected):
    assert list(itertools.accumulate(input)) == expected


@pytest.mark.parametrize("input, expected", [
    (["abc"], ["abc"]),
    (["ab", "def"], ["ab", "abdef"]),
    (["a", "bcde", "f"], ["a", "abcde", "abcdef"]),
    (["abc", "defgh", "", "ij"], ["abc", "abcdefgh", "abcdefgh", "abcdefghij"])
])
def test_accumulate_default_behaviour_strings(input, expected):
    assert list(itertools.accumulate(input)) == expected


@pytest.mark.parametrize("input, expected", [
    ([-23], [-23]),
    ([-1, -10], [-1, -11]),
    ([14, 3, -6], [14, 17, 11]),
    ([3, 16, 2, 43], [3, 19, 21, 64]),
])
def test_accumulate_default_behaviour_negative_numbers(input, expected):
    assert list(itertools.accumulate(input)) == expected


@pytest.mark.parametrize("input, expected", [
    ([12.4], [12.4]),
    ([19.1, -3.4], [19.1, 15.7]),
    ([4.2, -3.1, 2.1], [4.2, 1.1, 3.2]),
    ([23.1, -1.9, 10, 7.2], [23.1, 21.2, 31.2, 38.4])
])
def test_accumulate_default_behaviour_float_numbers(input, expected):
    assert pytest.approx(list(itertools.accumulate(input))) == expected


@pytest.mark.parametrize("input, exception_message", [
    ([1, "string"], "unsupported operand type(s) for +: 'int' and 'str'"),
    ([1.23, "string"], "unsupported operand type(s) for +: 'float' and 'str'"),
    (["string", 1], "can only concatenate str (not \"int\") to str"),
    (["string", 1.23], "can only concatenate str (not \"float\") to str"),
])
def test_accumulate_default_behaviour_invalid_type(input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.accumulate(input))
    assert excinfo.value.args[0] == exception_message


@pytest.mark.parametrize("input, expected", [
    ([], []),
    ([13.1], [13.1]),
    ([-2.3, 12.3], [-2.3, -28.29]),
    ([6, -2.1, 3.4], [6, -12.6, -42.84]),
    (["abc", 3], ["abc", "abcabcabc"]),
    ([2, "a"], [2, "aa"]),
    ([3, "ab", 2], [3, "ababab", "abababababab"])
])
def test_accumulate_func_multiplication(input, expected):
    assert pytest.approx(list(itertools.accumulate(input, func=operator.mul))) == expected


@pytest.mark.parametrize("input, exception_message", [
    ([1.23, "string"], "can't multiply sequence by non-int of type 'float'"),
    (["string", 1.23], "can't multiply sequence by non-int of type 'float'"),
    (["string", "string"], "can't multiply sequence by non-int of type 'str'"),
    (["string", 3, "string"], "can't multiply sequence by non-int of type 'str'"),
    ([3, "string", "string"], "can't multiply sequence by non-int of type 'str'"),
])
def test_accumulate_func_multiplication_invalid_type(input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.accumulate(input, func=operator.mul))
    assert excinfo.value.args[0] == exception_message


@pytest.mark.parametrize("input, expected", [
    ([], []),
    ([13.1], [13.1]),
    ([-2.3, 12.3], [-2.3, 12.3]),
    ([3, -2.1, 3.4], [3, 3, 3.4]),
    (["abcde"], ["abcde"]),
    (["abc", "bcd", "abd"], ["abc", "bcd", "bcd"]),
])
def test_accumulate_func_max(input, expected):
    assert pytest.approx(list(itertools.accumulate(input, func=max))) == expected


@pytest.mark.parametrize("input, exception_message", [
    ([1, "string"], "'>' not supported between instances of 'str' and 'int'"),
    (["string", 1], "'>' not supported between instances of 'int' and 'str'"),
    ([1.23, "string"], "'>' not supported between instances of 'str' and 'float'"),
    (["string", 1.23], "'>' not supported between instances of 'float' and 'str'"),
    (["string", 3, "string"], "'>' not supported between instances of 'int' and 'str'"),
    ([3, "string", "string"], "'>' not supported between instances of 'str' and 'int'"),
])
def test_accumulate_func_max_invalid_type(input, exception_message):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.accumulate(input, func=max))
    assert excinfo.value.args[0] == exception_message


@pytest.mark.parametrize("input, initial, expected", [
    ([], 1.2, [1.2]),
    ([13.1], 3, [3, 16.1]),
    ([-2.3, 12.3], -1.4, [-1.4, -3.7, 8.6]),
    ([], "abc", ["abc"]),
    (["def", "gh"], "abc", ["abc", "abcdef", "abcdefgh"])
])
def test_accumulate_initial_value(input, initial, expected):
    assert pytest.approx(list(itertools.accumulate(input, initial=initial))) == expected


@pytest.mark.parametrize("input, initial, exception_message", [
    ([1, 2], "string", "can only concatenate str (not \"int\") to str"),
    ([1.3, 2.5], "string", "can only concatenate str (not \"float\") to str"),
    (["abc", "def"], 3, "unsupported operand type(s) for +: 'int' and 'str'"),
    (["abc", "def"], 1.3, "unsupported operand type(s) for +: 'float' and 'str'")
])
def test_accumulate_initial_value_invalid_type(input, initial, exception_message):
    with pytest.raises(TypeError) as excinfo:
        list(itertools.accumulate(input, initial=initial))
    assert excinfo.value.args[0] == exception_message
