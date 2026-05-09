def process_mood(mood: str, interests_list: list) -> list:
    """
    Appends mood-specific prompt tags to the interest list, 
    shaping the LLM output toward the user's desired vibe.
    """
    mood = mood.strip()
    enhanced_interests = list(interests_list)
    
    if mood == "Relax":
        enhanced_interests.append("Prioritize quiet places, spas, scenic viewpoints, and late morning starts.")
    elif mood == "Adventure":
        enhanced_interests.append("Include high-adrenaline activities, hiking, water sports, and early morning starts.")
    elif mood == "Spiritual":
        enhanced_interests.append("Prioritize ancient temples, meditation spots, ashrams, and culturally significant monuments.")
    elif mood == "Party":
        enhanced_interests.append("Include popular clubs, vibrant nightlife, beach shacks, and evening social spots.")
        
    return enhanced_interests
