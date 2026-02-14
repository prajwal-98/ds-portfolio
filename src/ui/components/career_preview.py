# src/ui/components/career_preview.py
import streamlit as st
from src.ui.components.timeline_data import get_career_timeline_data

try:
    # Try the most common export name
    from streamlit_timeline import st_timeline as timeline
except ImportError:
    # Fallback to the alternative export name
    from streamlit_timeline import timeline

def render_career_preview():
    """
    Renders the interactive TimelineJS component with CSS fixes.
    """
    
    # --- CSS FIX: FORCE HEIGHT & REMOVE SCROLLBARS ---
    st.markdown("""
        <style>
            /* 1. Target the iframe specifically to force height */
            iframe.stWait {
                height: 600px !important;
                width: 100% !important;
            }
            
            /* 2. Ensure the container doesn't cut off the bottom (years) */
            .element-container {
                overflow: visible !important;
            }
            
            /* 3. Hide the internal Streamlit scrollbar for this block */
            iframe {
                border: none !important;
                overflow: hidden !important;
            }
        </style>
    """, unsafe_allow_html=True)

    # 1. Header
    st.markdown('<div style="margin-bottom: 20px;">', unsafe_allow_html=True)
    st.caption("Swipe or drag the timeline below to explore my journey.")
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Load Data
    data = get_career_timeline_data()

    # 3. Check Data
    if not data or "events" not in data:
        st.error("Timeline data is missing.")
        return

    # 4. Render Timeline
    # We use height=600 to ensure the bottom navigation bar is visible
    timeline(data, height=450)