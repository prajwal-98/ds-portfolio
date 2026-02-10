import streamlit as st
from src.ui.utils.theme import toggle_theme_mode

def render_navbar():
    current_mode = st.session_state.get("theme_mode", "light")
    theme_icon = "🌙" if current_mode == "light" else "☀️"
    
    # YOUR LOCKED WEIGHTS
    c1, c2, c3, c4, c5, spacer, c_theme = st.columns([0.6, 0.6, 1.3, 0.7, 1, 6, 0.6], gap="small")
    
    with c1:
        if st.button("Home", key="nav_home"):
            st.session_state.page = "Home"
            st.rerun()
    with c2:
        if st.button("About", key="nav_about"):
            st.session_state.page = "About"
            st.rerun()
    with c3:
        if st.button("Career Snapshot", key="nav_career"):
            st.session_state.page = "Career Snapshot"
            st.rerun()
    with c4:
        if st.button("Projects", key="nav_projects"):
            st.session_state.page = "Projects"
            st.rerun()
    with c5:
        if st.button("Resume", key="nav_resume"):
            st.session_state.page = "Resume"
            st.rerun()
            
    with c_theme:
        if st.button(theme_icon, key="theme_toggle"):
            toggle_theme_mode()
            st.rerun()
