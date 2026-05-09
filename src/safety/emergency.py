def get_emergency_intel(city: str) -> dict:
    """
    Mock logic that provides emergency intel based on the destination.
    A crucial socially-impactful feature.
    """
    city_lower = city.lower().strip()
    
    # Generic defaults
    intel = {
        "Nearest Hospital": f"City Care Hospital, Central {city.title()}",
        "Police Station": f"Main Branch Police Station, {city.title()}",
        "Emergency Number": "112 (National Emergency), 108 (Ambulance)",
        "Safety Tip": "Always share your live location with a trusted contact."
    }
    
    if city_lower in ["delhi", "mumbai"]:
        intel["Safety Tip"] = "Use official Cab options from Apps. Avoid unverified late-night autos."
    elif city_lower in ["goa", "kerala", "andaman"]:
        intel["Safety Tip"] = "Follow local beach safety flags. Do not swim at night or in unmarked zones."
    elif city_lower in ["manali", "shimla", "kashmir", "leh"]:
        intel["Safety Tip"] = "Carry thermal wear. Beware of altitude sickness and check weather before driving passes."
        
    return intel
