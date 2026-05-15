# BUG 4: Incorrect import path. Should be: from validator import validate_transaction
# (Or missing dot, or trying to import from a nonexistent 'src' directory)
from .validator import validate_transaction 
from calculator import calculate_total
from report import generate_text_report

def main():
    print("Welcome to Personal Finance Tracker")
    
    # Sample data
    sample_data = [
        {"amount": 50.0, "category": "Food", "type": "expense", "date": "2026-05-01"},
        {"amount": 120.0, "category": "Utilities", "type": "expense", "date": "2026-05-02"},
        {"amount": 30.0, "category": "Food", "type": "expense", "date": "2026-05-03"}
    ]
    
    valid_transactions = []
    for tx in sample_data:
        if validate_transaction(tx):
            valid_transactions.append(tx)
            
    print(generate_text_report(valid_transactions))

if __name__ == "__main__":
    main()
