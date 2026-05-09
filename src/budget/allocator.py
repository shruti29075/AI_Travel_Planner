def allocate_budget(total_budget: float) -> dict:
    """
    Dynamic percentage-based budget allocation based on the PRD:
    - Travel: 25%
    - Hotel: 30%
    - Food: 20%
    - Activities: 15%
    - Buffer/Emergency: 10%
    """
    return {
        "Travel": round(total_budget * 0.25, 2),
        "Hotel": round(total_budget * 0.30, 2),
        "Food": round(total_budget * 0.20, 2),
        "Activities": round(total_budget * 0.15, 2),
        "Buffer/Emergency": round(total_budget * 0.10, 2),
    }
