def calculate_total(transactions: list) -> float:
    """Calculates the net balance from a list of validated transactions.

    Transactions tagged with ``type == "expense"`` are subtracted from the
    balance; all others (income, unspecified, or any other type) are added.
    Amounts themselves are always treated as magnitudes — the sign is derived
    from ``type`` so callers don't have to encode it twice.
    """
    total = 0.0
    for t in transactions:
        amount = t["amount"]
        if t.get("type") == "expense":
            total -= amount
        else:
            total += amount
    return total

def calculate_average(transactions: list) -> float:
    """Calculates the average transaction amount."""
    total = calculate_total(transactions)
    
    # BUG 2: Missing check for empty list. 
    # Should be: if len(transactions) == 0: return 0.0
    return total / len(transactions)

def group_by_category(transactions: list) -> dict:
    """Groups transaction amounts by their category."""
    category_totals = {}
    for t in transactions:
        cat = t["category"]
        category_totals[cat] = category_totals.get(cat, 0.0) + t["amount"]
    return category_totals
