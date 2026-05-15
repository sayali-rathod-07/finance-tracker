import pytest
from calculator import calculate_total, calculate_average, group_by_category

def test_calculate_total():
    txs = [
        {"amount": 10.0, "category": "A"},
        {"amount": 20.5, "category": "B"}
    ]
    assert calculate_total(txs) == 30.5

def test_calculate_average_empty():
    # This test will FAIL initially with ZeroDivisionError due to Bug 2
    assert calculate_average([]) == 0.0

def test_group_by_category():
    txs = [
        {"amount": 10.0, "category": "Food"},
        {"amount": 15.0, "category": "Food"},
        {"amount": 20.0, "category": "Gas"}
    ]
    result = group_by_category(txs)
    assert result["Food"] == 25.0
    assert result["Gas"] == 20.0
