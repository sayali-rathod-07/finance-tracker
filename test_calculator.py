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

def test_calculate_total_deducts_expenses():
    txs = [
        {"amount": 1000.0, "category": "Salary", "type": "income"},
        {"amount": 200.0, "category": "Food", "type": "expense"},
        {"amount": 50.0, "category": "Gas", "type": "expense"},
    ]
    assert calculate_total(txs) == 750.0

def test_calculate_total_pure_expenses():
    txs = [
        {"amount": 30.0, "category": "Food", "type": "expense"},
        {"amount": 70.0, "category": "Utilities", "type": "expense"},
    ]
    assert calculate_total(txs) == -100.0

def test_calculate_total_empty():
    assert calculate_total([]) == 0.0

def test_calculate_total_missing_type_defaults_to_additive():
    # Backward compatibility: untyped transactions are added (preserves
    # the original sum-everything behavior callers may still rely on).
    txs = [{"amount": 10.0, "category": "A"}, {"amount": 20.5, "category": "B"}]
    assert calculate_total(txs) == 30.5

def test_group_by_category():
    txs = [
        {"amount": 10.0, "category": "Food"},
        {"amount": 15.0, "category": "Food"},
        {"amount": 20.0, "category": "Gas"}
    ]
    result = group_by_category(txs)
    assert result["Food"] == 25.0
    assert result["Gas"] == 20.0
