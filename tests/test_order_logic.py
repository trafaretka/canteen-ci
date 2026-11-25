import pytest
from src.order_logic import calculate_total, is_preorder_available


def test_calculate_total_no_discount():
    assert calculate_total([100.0, 50.5]) == 150.5


def test_calculate_total_with_discount():
    assert calculate_total([200.0, 100.0], discount_percent=10) == 270.0


def test_calculate_total_invalid_discount():
    with pytest.raises(ValueError):
        calculate_total([100.0], discount_percent=150)


def test_is_preorder_available():
    assert is_preorder_available(12) is True
    assert is_preorder_available(20) is False
