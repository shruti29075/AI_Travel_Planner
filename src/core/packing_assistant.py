def generate_packing_list(city: str, mood: str, days: int) -> list:
    """
    Suggests clothes and essentials based on location and trip mood.
    """
    city_lower = city.lower().strip()
    
    list_items = [
        "Original ID Proof (Aadhar/Passport) & printed copies.",
        "Personal Medications & Basic First Aid Kit.",
        "Portable Power Bank & Multi-plug Adapter."
    ]
    
    # Mood based
    if mood == "Adventure":
        list_items.extend(["Trekking shoes / Sturdy footwear.", "Bug repellent & Sunscreen.", "Waterproof backpack cover."])
    elif mood == "Party":
        list_items.extend(["Party wear / Smart Casuals.", "Hangover remedies (Eno, hydration salts).", "Extra cash for cover charges."])
    elif mood == "Relax":
        list_items.extend(["Comfortable lounging clothes.", "A good book or Kindle.", "Swimwear (if hotel has pool)."])
    elif mood == "Spiritual":
        list_items.extend(["Modest clothing covering shoulders and knees.", "Scarf / Head cover for temples.", "Slip-on shoes for frequent removal."])
    
    # Location based
    if city_lower in ["manali", "shimla", "kashmir", "leh"]:
        list_items.extend(["Heavy Winter Jacket & thermals.", "Woolen socks & gloves.", "Moisturizers & lip balm."])
    elif city_lower in ["goa", "kerala", "andaman", "gokarna"]:
        list_items.extend(["Sunglasses & Beach hat.", "Swimwear & Flip-flops.", "Aloe Vera gel."])
    elif city_lower in ["delhi", "mumbai", "kolkata"]:
        list_items.extend(["Pollution mask (N95).", "Light, breathable cotton clothes."])
        
    return list_items
