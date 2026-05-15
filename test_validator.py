import pytest
from validator import validate_transaction

def test_valid_transaction():
    tx = {"amount": 50.0, "category": "Food", "date": "2026-05-01"}
    assert validate_transaction(tx) is True

def test_missing_keys():
    tx = {"amount": 50.0, "category": "Food"}
    assert validate_transaction(tx) is False

def test_negative_amount():
    # This test will FAIL initially due to Bug 3
    tx = {"amount": -50.0, "category": "Food", "date": "2026-05-01"}
    assert validate_transaction(tx) is False
