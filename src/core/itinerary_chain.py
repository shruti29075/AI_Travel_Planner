# src/core/itinerary_chain.py
from src.core.planner import TIME_SLOTS
from src.chains.ai_suggester import get_spot_description

def generate_itinerary(city: str, day_wise_spots: list[list[str]]):
    output = [f"✨ {city.title()} Travel Itinerary\n"]

    for day_no, spots in enumerate(day_wise_spots, start=1):
        output.append(f"🟦 DAY {day_no} – {city.title()} Highlights\n")
        for slot, place in zip(TIME_SLOTS, spots):
            desc = get_spot_description(city, place)
            output.append(f"{slot}: {place}\n{desc}\n")
        output.append("\n")
    return "\n".join(output)
