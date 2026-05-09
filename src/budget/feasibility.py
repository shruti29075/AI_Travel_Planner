def validate_budget(total_budget: float, num_days: int, num_people: int) -> dict:
    """
    Checks if the user's budget is realistic.
    Assumes a minimum threshold of ₹1500 per person per day for survival.
    """
    MIN_COST_PER_PERSON_PER_DAY = 1500
    required_min_budget = MIN_COST_PER_PERSON_PER_DAY * num_days * num_people
    
    if total_budget < required_min_budget:
        return {
            "feasible": False,
            "message": f"⚠ Minimum recommended budget for a {num_days}-day trip for {num_people} people is ₹{required_min_budget}. Your budget of ₹{total_budget} is too low.",
            "min_required": required_min_budget
        }
    
    return {
        "feasible": True,
        "message": "✅ Budget is feasible.",
        "min_required": required_min_budget
    }
