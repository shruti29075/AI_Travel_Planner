import random

def generate_smart_alerts(city: str) -> list:
    """
    Predictive intelligence alerts (mock implementation imitating time-series logic).
    """
    city_lower = city.lower().strip()
    alerts = []
    
    # Randomly predict rain or weather alerts 1 in 3 times
    if random.choice([True, False, False]):
        alerts.append("🌦️ **Weather AI:** Light rain expected on Day 2. We recommend scheduling museums or indoor activities then.")
        
    # City specific crowd alerts
    if city_lower in ["goa", "kasol", "kushalnagar", "manali"]:
        alerts.append("🚦 **Crowd AI:** High tourist influx expected over the weekend. Book popular restaurants at least 1 day in advance.")
        
    # Transit alerts
    if city_lower in ["mumbai", "delhi", "bengaluru"]:
        alerts.append("⏰ **Time-Saver AI:** Extreme peak-hour traffic detected between 9 AM - 11 AM and 6 PM - 8 PM. Avoid road transit during these hours to save up to 2 hours of transit time.")
        
    # Hidden cost detector
    if random.choice([True, False]):
        alerts.append("💰 **Hidden Cost AI:** Tourist spots in this destination often have unexpected camera/phablet entry fees. Kept an extra ₹500 in buffer.")

    if not alerts:
        alerts.append("✅ **AI Scan Clear:** No unusual weather, traffic, or surge pricing detected for your dates.")
        
    return alerts
