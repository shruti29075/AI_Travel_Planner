import streamlit as st

# Must be the first Streamlit command
st.set_page_config(page_title="TripGenius - Pro Max Planner", layout="wide")

from src.core.planner import TravelPlanner
from src.core.itinerary_chain import generate_itinerary
from src.chains.ai_suggester import suggest_spots_for_city, llm
from src.chains.chat_assistant import get_chat_response
from pdf_generate import generate_pdf
from src.ui.auth_ui import show_auth_page

# Phase 2 Core logic imports
from src.budget.feasibility import validate_budget
from src.budget.allocator import allocate_budget
from src.transport.travel_type import suggest_travel_type
from src.transport.micro_mobility import suggest_micro_mobility

# Phase 3 & 4 Pro Max logic imports
from src.safety.emergency import get_emergency_intel
from src.core.packing_assistant import generate_packing_list
from src.core.mood_engine import process_mood
from src.core.smart_alerts import generate_smart_alerts

def show_main_app():
    st.title("🧳 TripGenius Pro Max - AI Travel Co-Pilot")
    
    # ---------------- Header with Logout ----------------
    col1, col2 = st.columns([8, 1])
    with col1:
        st.write(f"Welcome back, **{st.session_state.get('username')}**! Ready for your next adventure?")
    with col2:
        if st.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = None
            st.session_state["user_id"] = None
            st.rerun()
            
    st.markdown("---")

    # ---------------- Sidebar ----------------
    st.sidebar.header("Enter Trip Details")
    city = st.sidebar.text_input("Destination (City Name)", "")
    days = st.sidebar.slider("Trip Duration (in Days)", 1, 7, 4)
    trip_mood = st.sidebar.selectbox("Trip Mood / Vibe", ["Relax", "Adventure", "Spiritual", "Party"])

    # ---------------- Session State ----------------
    if "interests" not in st.session_state:
        st.session_state["interests"] = ""
    if "prev_city" not in st.session_state:
        st.session_state["prev_city"] = ""
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

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
        height=150
    )

    # ---------------- Budget ----------------
    total_budget = st.sidebar.number_input("Total Budget (INR)", min_value=0, value=15000, step=500)
    trip_type = st.sidebar.radio("Trip Type", ["Solo", "Group", "Family"])
    num_people = 1
    if trip_type == "Group" or trip_type == "Family":
        num_people = st.sidebar.number_input("Number of People", min_value=2, value=2)
    per_person_budget = total_budget / num_people if num_people > 0 else total_budget
    daily_pp_budget = per_person_budget / days if days > 0 else 0

    # ---------------- Budget Feasibility Check ----------------
    feasibility_res = validate_budget(total_budget, days, num_people)
    if not feasibility_res["feasible"]:
        st.sidebar.error(feasibility_res["message"])
        can_generate = False
    else:
        st.sidebar.success(feasibility_res["message"])
        can_generate = True

    # ---------------- Generate Itinerary ----------------
    if st.sidebar.button("✨ Generate AI Smart Plan"):
        if not can_generate:
            st.error("Cannot generate itinerary. Please increase your budget to meet the minimum feasibility criteria.")
        elif not city.strip():
            st.error("Please enter a city name.")
        else:
            # Clear chat history on new generation
            st.session_state["chat_history"] = []

            # Phase 2 Computations
            budget_alloc = allocate_budget(total_budget)
            travel_type_suggestion = suggest_travel_type(per_person_budget, num_people)
            micro_mobility_sug = suggest_micro_mobility(city, daily_pp_budget)

            # Phase 3 Computations
            raw_interests = [i.strip() for i in interests_input.split(",") if i.strip()]
            mood_interests = process_mood(trip_mood, raw_interests) # Apply mood
            
            emergency_intel = get_emergency_intel(city)
            packing_list = generate_packing_list(city, trip_mood, days)
            smart_alerts = generate_smart_alerts(city)

            planner = TravelPlanner()
            day_wise_spots = planner.split_days(mood_interests, days)
            itinerary_text = generate_itinerary(city, day_wise_spots)

            # --- Storing into session state ---
            st.session_state["itinerary_text"] = itinerary_text
            st.session_state["city"] = city
            st.session_state["budget_alloc"] = budget_alloc
            st.session_state["total_budget"] = total_budget
            st.session_state["num_people"] = num_people
            st.session_state["per_person_budget"] = per_person_budget
            st.session_state["travel_type_suggestion"] = travel_type_suggestion
            st.session_state["micro_mobility_sug"] = micro_mobility_sug
            st.session_state["emergency_intel"] = emergency_intel
            st.session_state["packing_list"] = packing_list
            st.session_state["smart_alerts"] = smart_alerts

            # Final PDF compiler
            pdft = f"---- TRIP ITINERARY ({trip_mood.upper()} VIBE) ----\n\n" + itinerary_text + "\n\n"
            pdft += "---- BUDGET SUMMARY ----\n"
            pdft += f"Total: Rs {total_budget} | Per Person: Rs {per_person_budget:.2f}\n\n"
            pdft += "---- SMART ALERTS ----\n" + "\n".join(smart_alerts)
            st.session_state["final_pdf_text"] = pdft
            
            st.success("✅ AI Trip Plan Generated Successfully!")

    # ---------------- Display Results ----------------
    if "itinerary_text" in st.session_state:
        
        tab1, tab2, tab3, tab4 = st.tabs([
            "🗓️ Itinerary", 
            "📈 Travel Score Dashboard", 
            "🚀 Pro Max Intelligence",
            "💬 AI Co-Pilot"
        ])
        
        with tab1:
            st.markdown(f"## {days}-Day Itinerary for **{st.session_state['city'].title()}**")
            st.info(f"✨ Geoclustering Applied. Powered by **{trip_mood}** Mood Engine.")
            st.markdown(st.session_state["itinerary_text"])
            
        with tab2:
            st.markdown("## 📊 Gamification & Analytics")
            col_a, col_b, col_c = st.columns(3)
            col_a.metric("Budget Utilization", "85%", "+15% Buffer left")
            col_b.metric("Time Efficiency Score", "92/100", "Geo-Clustered")
            col_c.metric("Sustainability Rating", "Eco-Friendly", "+20 Karma Points")
            
            st.markdown("### 💼 Automated Budget Allocation")
            for k, v in st.session_state["budget_alloc"].items():
                st.write(f"- **{k}**: ₹{v}")
                
            st.markdown("### 🚗 Transport Suggestions")
            st.write(f"**Travel Type**: {st.session_state['travel_type_suggestion']['type']} ({st.session_state['travel_type_suggestion']['description']})")
            st.write(f"**Local Commute**: {st.session_state['micro_mobility_sug']}")
            
        with tab3:
            st.markdown("## 🔮 Predictive Trip Intelligence")
            for idx, alert in enumerate(st.session_state["smart_alerts"]):
                st.warning(alert)
                
            st.markdown("---")
            col_packs, col_emg = st.columns(2)
            with col_packs:
                st.markdown("### 🎒 Smart Packing Assistant")
                for item in st.session_state["packing_list"]:
                    st.write(f"✔️ {item}")
                    
            with col_emg:
                st.markdown("### 🚨 Emergency Contacts")
                for key, val in st.session_state["emergency_intel"].items():
                    st.write(f"**{key}**: {val}")
                    
        with tab4:
            st.markdown("## 💬 Talk to your Travel Co-Pilot")
            st.write("Need changes? Ask me for nearby food, alternative spots, or hidden costs!")
            
            for msg in st.session_state["chat_history"]:
                with st.chat_message(msg["role"]):
                    st.markdown(msg["content"])
                    
            if user_msg := st.chat_input("E.g., What should I eat for lunch on Day 1?"):
                st.session_state["chat_history"].append({"role": "user", "content": user_msg})
                with st.chat_message("user"):
                    st.markdown(user_msg)
                    
                with st.chat_message("assistant"):
                    with st.spinner("Thinking..."):
                        bot_response = get_chat_response(llm, st.session_state["itinerary_text"], user_msg)
                        st.markdown(bot_response)
                st.session_state["chat_history"].append({"role": "assistant", "content": bot_response})
            
        st.markdown("---")
        st.subheader("📄 Export Plan")
        filename = f"{st.session_state['city']}_trip.pdf"
        generate_pdf(st.session_state["final_pdf_text"], filename)
        with open(filename, "rb") as f:
            st.download_button(label="Download PDF", data=f, file_name=filename, mime="application/pdf")

if __name__ == "__main__":
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if not st.session_state["logged_in"]:
        show_auth_page()
    else:
        show_main_app()
