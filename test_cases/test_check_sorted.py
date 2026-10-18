
import pytest
import importlib

module = importlib.import_module("codes.check_sorted")


def test_sorted_list():
    assert module.is_sorted([1, 2, 2, 4, 5]) is True


def test_unsorted_list():
    assert module.is_sorted([1, 4, 3, 5]) is False


def test_empty_list():
    assert module.is_sorted([]) is True


def test_single_element_list():
    assert module.is_sorted([10]) is True


def test_all_equal_elements():
    assert module.is_sorted([3, 3, 3, 3]) is True


def test_descending_list():
    assert module.is_sorted([5, 4, 3, 2, 1]) is False


def test_negative_numbers():
    assert module.is_sorted([-5, -3, -1, 0, 2]) is True


def test_mixed_negative_and_positive_numbers():
    assert module.is_sorted([-3, -1, 2, 1]) is False


def test_two_sorted_elements():
    assert module.is_sorted([1, 2]) is True


def test_two_unsorted_elements():
    assert module.is_sorted([2, 1]) is False


def test_list_with_zero():
    assert module.is_sorted([-1, 0, 0, 2]) is True


def test_invalid_string_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        module.is_sorted("123")


def test_invalid_integer_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        module.is_sorted(123)


def test_invalid_none_input():
    with pytest.raises(TypeError, match="Input must be a list"):
        module.is_sorted(None)
