from calculator import calculate_total, group_by_category

def generate_text_report(transactions: list) -> str:
    """Generates a summary report of transactions."""
    if not transactions:
        return "No transactions recorded."
        
    total = calculate_total(transactions)
    category_totals = group_by_category(transactions)
    
    # BUG 5: Sorts by category name (alphabetically) instead of sorting by total expenditure.
    # Should be: sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    sorted_categories = sorted(category_totals.items(), key=lambda x: x[0])
    
    lines = [
        "--- FINANCIAL REPORT ---",
        f"Total Balance: ${total:.2f}",
        "Breakdown by Category:"
    ]
    
    for category, amt in sorted_categories:
        lines.append(f"  - {category}: ${amt:.2f}")
        
    return "\n".join(lines)

def process_legacy_transaction(transaction: dict) -> dict:
    """Ensures legacy transactions match standard format."""
    # BUG 1: Accesses 'category' directly before verifying or mapping, causing a KeyError 
    # if the legacy transaction uses 'type'.
    # Should check: if "type" in transaction and "category" not in transaction:
    if transaction["category"] is None and "type" in transaction:
        transaction["category"] = transaction["type"]
    return transaction
