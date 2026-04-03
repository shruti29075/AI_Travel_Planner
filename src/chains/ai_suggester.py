# src/chains/ai_suggester.py
import os
import re
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# ----------------- Initialize Groq -----------------
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
llm = None
spot_prompt = None
desc_prompt = None

if GROQ_API_KEY:
    try:
        llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name="llama-3.3-70b-versatile",
            temperature=0.3,
            top_p=0.9,
            max_tokens=800
        )

        # Spot list prompt
        spot_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "List top 10 famous tourist places to visit in {city}. "
             "Give exact spot names people visit, no generic names. "
             "Output as comma separated list only."),
            ("human", "Give the list now.")
        ])

        # Spot description prompt
        desc_prompt = ChatPromptTemplate.from_messages([
            ("system",
             "Provide a short, clear description why {spot} is famous in {city}. "
             "Keep it 1-2 lines for tourists.")
        ])
    except Exception:
        llm = None


# ----------------- Helpers -----------------
def _parse_spots(text: str):
    lines = [l.strip() for l in text.splitlines() if l.strip()]
    cleaned = []
    for l in lines:
        cleaned.extend(re.split(r'[,;\n]+', re.sub(r'^[\-\d\.\)\s]+', '', l)))
    return [c.strip() for c in cleaned if c.strip()]


# ----------------- Main Functions -----------------
def suggest_spots_for_city(city: str):
    if not city or not llm or not spot_prompt:
        return []

    try:
        messages = spot_prompt.format_messages(city=city)
        resp = llm.invoke(messages)
        text = resp.content if hasattr(resp, "content") else str(resp)
        return _parse_spots(text)[:10]
    except Exception:
        return []


def get_spot_description(city: str, spot: str):
    if not city or not spot or not llm or not desc_prompt:
        return "Popular spot worth visiting."
    try:
        messages = desc_prompt.format_messages(city=city, spot=spot)
        resp = llm.invoke(messages)
        text = resp.content if hasattr(resp, "content") else str(resp)
        return text.strip()
    except Exception:
        return "Popular spot worth visiting."
