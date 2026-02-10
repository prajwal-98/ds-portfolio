import streamlit as st
from streamlit_timeline import timeline
from src.ui.components.timeline_data import get_career_timeline_data

def render_career_snapshot():
    """
    Renders the interactive TimelineJS component.
    """
    
    # 1. Header
    st.markdown('<div style="margin-bottom: 30px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("""
        <h1 style="text-align: center;">Career Snapshot</h1>
        <p style="text-align: center; color: var(--text-secondary);">
            Drag the slider below to explore my journey.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Load Data
    data = get_career_timeline_data()

    # 3. Render Timeline
    # We store the return value
    timeline_event = timeline(data, height=600)
    
    # 4. Interaction Logic (Safe Mode)
    # We check if it is NOT None and IS a Dictionary before using .get()
    if timeline_event and isinstance(timeline_event, dict):
        # Extract headline safely
        headline = timeline_event.get("text", {}).get("headline", "Selected Event")
        st.info(f"**Selected:** {headline}")
    else:
        # Fallback if nothing is selected or if it returns a render object
        st.caption("Swipe or drag the timeline to view details.")
