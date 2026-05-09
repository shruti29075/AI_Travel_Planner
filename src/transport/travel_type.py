def suggest_travel_type(budget_per_person: float, num_people: int) -> dict:
    """
    Suggests the optimal mode of travel based on budget and group size.
    """
    if budget_per_person > 10000:
        return {
            "type": "Private Travel",
            "description": "Premium experience. Private cabs & exclusive stays."
        }
    elif num_people > 2 and budget_per_person > 4000:
        return {
            "type": "Known Group Travel",
            "description": "Shared costs among known members. Rental cars/SUVs."
        }
    elif budget_per_person < 4000:
        return {
            "type": "Public Travel",
            "description": "Low-cost. Trains, Metro, and local buses recommended."
        }
    else:
        return {
            "type": "Unknown Group Travel",
            "description": "Agency-based package tour for optimal costing."
        }
