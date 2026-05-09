def suggest_micro_mobility(city: str, daily_budget: float) -> str:
    """
    Suggest micro-mobility options comparing cab costs vs rentals based on rough heuristics.
    """
    metros = ["delhi", "mumbai", "bengaluru", "kolkata", "chennai", "hyderabad", "pune"]
    city_lower = city.lower().strip()
    
    if daily_budget < 1000:
        if city_lower in metros:
            return "Metro Pass & Local Bus Pass highly recommended. Minimize cab usage."
        else:
            return "Local bus or walking routes recommended."
            
    if daily_budget < 2500:
       return "Bike/Scooty rental is optimal. Much cheaper than multiple Cabs per day."
       
    return "Cabs (Uber/Ola) are feasible within your budget. No strict need for rentals unless preferred."
