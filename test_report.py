import pytest
from report import generate_text_report, process_legacy_transaction

def test_legacy_transaction_key_error():
    # This test will FAIL initially with KeyError due to Bug 1
    legacy_tx = {"amount": 45.0, "type": "Groceries", "date": "2026-05-01"}
    processed = process_legacy_transaction(legacy_tx)
    assert processed["category"] == "Groceries"

def test_report_sorting():
    # This test will FAIL initially due to Bug 5 
    # (It sorts alphabetically [Food, Utilities] instead of by highest expenditure [Utilities, Food])
    txs = [
        {"amount": 10.0, "category": "Food"},
        {"amount": 150.0, "category": "Utilities"}
    ]
    report = generate_text_report(txs)
    
    # Utilities should appear before Food because 150 > 10
    utilities_index = report.find("Utilities")
    food_index = report.find("Food")
    assert utilities_index < food_index
