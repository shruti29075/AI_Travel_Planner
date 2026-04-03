# src/core/planner.py
import math

TIME_SLOTS = [
    "6:30 AM - 8:00 AM",
    "9:00 AM - 10:30 AM",
    "11:00 AM - 12:30 PM",
    "1:30 PM - 3:00 PM",
    "4:00 PM - 5:30 PM",
    "6:00 PM - 7:30 PM"
]

class TravelPlanner:
    def merge_spots(self, user_spots, ai_spots):
        combined = []
        for s in (user_spots or []):
            if s and s not in combined:
                combined.append(s)
        for s in (ai_spots or []):
            if s and s not in combined:
                combined.append(s)
        return combined[:10]

    def split_days(self, spots, days):
        if days <= 0:
            days = 1
        per_day = max(1, math.ceil(len(spots) / days))
        return [spots[i:i + per_day] for i in range(0, len(spots), per_day)]
