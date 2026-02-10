# src/ui/pages/career_snapshot.py
import streamlit as st
from src.ui.components.career_preview import render_career_preview

def render_career_snapshot():
    st.title("📈 Career Snapshot")
    
    # Render the component
    render_career_preview()

    # Footer
    st.markdown("---")
    st.caption("🚀 *Always learning, always building.*")