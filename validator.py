def validate_transaction(transaction: dict) -> bool:
    """
    Validates a transaction dictionary.
    Required keys: 'amount', 'category', 'date'
    Amount must be a positive number.
    """
    required_keys = ["amount", "category", "date"]
    for key in required_keys:
        if key not in transaction:
            return False
            
    # BUG 3: Allows negative amounts. Should check: isinstance(transaction["amount"], (int, float)) and transaction["amount"] > 0
    if not isinstance(transaction["amount"], (int, float)):
        return False
        
    return True
