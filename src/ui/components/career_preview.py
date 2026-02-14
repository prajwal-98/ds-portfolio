# src/ui/components/career_preview.py
import streamlit as st
from src.ui.components.timeline_data import get_career_timeline_data

# --- SAFE IMPORT ---
try:
    from streamlit_timeline import st_timeline as timeline
except ImportError:
    try:
        from streamlit_timeline import timeline
    except ImportError:
        timeline = None

def render_career_preview():
    """
    Renders the interactive TimelineJS with a safe fallback for PermissionErrors.
    """
    
    # --- 1. CSS FIXES ---
    st.markdown("""
        <style>
            iframe { height: 600px !important; width: 100% !important; border: none !important; }
            .element-container { overflow: visible !important; }
            .static-card {
                padding: 1.5rem;
                border-radius: 12px;
                border: 1px solid #eee;
                margin-bottom: 1rem;
                background: white;
            }
        </style>
    """, unsafe_allow_html=True)

    # --- 2. LOAD DATA ---
    data = get_career_timeline_data()
    if not data or "events" not in data:
        st.error("Timeline data is missing.")
        return

    # --- 3. RENDER LOGIC ---
    try:
        # We attempt the interactive timeline first
        st.caption("Swipe or drag the timeline below to explore my journey.")
        timeline(data, height=450)
        
    except Exception as e:
        # --- FALLBACK: PROFESSIONAL STATIC LIST ---
        st.info("💡 Visual timeline is loading... (Showing summarized view)")
        
        for event in data["events"]:
            # Extracting data from the TimelineJS JSON structure
            text_data = event.get("text", {})
            date_data = event.get("start_date", {})
            
            title = text_data.get("headline", "Experience")
            desc = text_data.get("text", "")
            year = f"{date_data.get('year', '')}"
            
            with st.container():
                st.markdown(f"""
                <div class="static-card">
                    <span style="color: var(--accent); font-weight: 700;">{year}</span>
                    <h3 style="margin: 0; padding: 5px 0;">{title}</h3>
                    <div style="font-size: 0.95rem; color: #555;">{desc}</div>
                </div>
                """, unsafe_allow_html=True)