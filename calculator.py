def calculate_total(transactions: list) -> float:
    """Calculates total spending from a list of validated transactions."""
    return sum(t["amount"] for t in transactions)

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
