import streamlit as st
from src.auth.auth_manager import register_user, login_user


def _safe_rerun():
    """Support rerun across Streamlit versions."""
    if hasattr(st, "rerun"):
        st.rerun()
    elif hasattr(st, "experimental_rerun"):
        st.experimental_rerun()

def show_auth_page():
    st.title("🧳 TripGenius - Smart Trip Planner")
    st.subheader("Welcome! Please log in or sign up to continue.")
    
    tab1, tab2 = st.tabs(["Login", "Sign Up"])
    
    with tab1:
        st.write("### Login")
        login_username = st.text_input("Username", key="login_username")
        login_password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if login_username and login_password:
                user = login_user(login_username, login_password)
                if user:
                    st.session_state["user_id"] = user["id"]
                    st.session_state["username"] = user["username"]
                    st.session_state["logged_in"] = True
                    st.success("Logged in successfully!")
                    _safe_rerun()
                else:
                    st.error("Invalid username or password.")
            else:
                st.warning("Please enter both username and password.")

    with tab2:
        st.write("### Sign Up")
        reg_username = st.text_input("Username", key="reg_username")
        reg_password = st.text_input("Password", type="password", key="reg_password")
        reg_confirm = st.text_input("Confirm Password", type="password", key="reg_confirm")
        
        if st.button("Sign Up"):
            if reg_username and reg_password and reg_confirm:
                if reg_password == reg_confirm:
                    if register_user(reg_username, reg_password):
                        st.success("Account created successfully! You can now log in.")
                    else:
                        st.error("Username already exists. Please choose a different one.")
                else:
                    st.error("Passwords do not match.")
            else:
                st.warning("Please fill out all fields.")
