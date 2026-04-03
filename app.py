import streamlit as st
from src.core.planner import TravelPlanner
from src.core.itinerary_chain import generate_itinerary
from src.chains.ai_suggester import suggest_spots_for_city
from pdf_generate import generate_pdf

st.set_page_config(page_title="TripGenius - Smart Trip Planner", layout="wide")
st.title("🧳 TripGenius - Smart Trip Planner")

# ---------------- Sidebar ----------------
st.sidebar.header("Enter Trip Details")
city = st.sidebar.text_input("Destination (City Name)", "")
days = st.sidebar.slider("Trip Duration (in Days)", 1, 7, 4)

# ---------------- Session State ----------------
if "interests" not in st.session_state:
    st.session_state["interests"] = ""
if "prev_city" not in st.session_state:
    st.session_state["prev_city"] = ""

# ---------------- AI SPOTS ----------------
ai_spots = []
if city.strip() and city.lower() != st.session_state["prev_city"].lower():
    ai_spots = suggest_spots_for_city(city)
    if not ai_spots:
        st.warning("⚠️ AI could not fetch exact famous places. Check GROQ_API_KEY / internet.")
    st.session_state["interests"] = ", ".join(ai_spots)
    st.session_state["prev_city"] = city

interests_input = st.sidebar.text_area(
    "Enter your Interests / Spots:",
    value=st.session_state["interests"],
    height=200
)

# ---------------- Budget ----------------
total_budget = st.sidebar.number_input("Total Budget (INR)", min_value=0, value=5000, step=500)
trip_type = st.sidebar.radio("Trip Type", ["Solo", "Group", "Family"])
num_people = 1
if trip_type == "Group":
    num_people = st.sidebar.number_input("Number of People", min_value=2, value=2)
per_person_budget = total_budget / num_people if num_people > 0 else total_budget

# ---------------- Generate Itinerary ----------------
if st.sidebar.button("✨ Generate Itinerary"):
    if not city.strip():
        st.error("Please enter a city name.")
    else:
        interests_list = [i.strip() for i in interests_input.split(",") if i.strip()]
        planner = TravelPlanner()
        day_wise_spots = planner.split_days(interests_list, days)
        itinerary_text = generate_itinerary(city, day_wise_spots)

        st.session_state["final_pdf_text"] = (
            "---- TRIP ITINERARY ----\n\n" +
            itinerary_text +
            "\n\n---- BUDGET SUMMARY ----\n\n" +
            f"Total Budget: ₹{total_budget}\n"
            f"Number of People: {num_people}\n"
            f"Per Person Budget: ₹{per_person_budget:.2f}\n"
        )

        st.session_state["itinerary_text"] = itinerary_text
        st.session_state["city"] = city

        st.success("✅ Trip Plan Generated!")
        st.markdown(f"## 🗓️ {days}-Day Itinerary for **{city.title()}**")
        st.markdown(itinerary_text)

# ---------------- Download PDF ----------------
if "itinerary_text" in st.session_state:
    st.markdown("---")
    st.subheader("💰 Trip Budget Summary")
    st.markdown(f"""
    **Total Budget:** ₹ {total_budget}  
    **Number of People:** {num_people}  
    **Per Person Budget:** ₹ {per_person_budget:.2f}
    """)
    st.subheader("📄 Download Your Trip Plan")

    filename = f"{st.session_state['city']}_trip.pdf"
    generate_pdf(st.session_state["final_pdf_text"], filename)
    with open(filename, "rb") as f:
        st.download_button(label="Download PDF", data=f, file_name=filename, mime="application/pdf")
