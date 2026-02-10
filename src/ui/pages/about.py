import streamlit as st
from src.ui.components.about_cards import render_interactive_cards

def render_about():
    """
    Final Locked About Page Structure:
    1. Professional Intro (Text)
    2. Interactive Cards Grid (Skills, Photo, Milestones)
    """
    
    # 1. Page Header & Intro
    # Uses the same spacing rules as Home (80px bottom margin)
    st.markdown('<div style="margin-bottom: 60px; padding: 0 1rem;">', unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .about-header {
            font-size: 3rem;
            font-weight: 800;
            margin-bottom: 1.5rem;
            background: linear-gradient(135deg, var(--text) 0%, var(--text-secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .about-sub {
            font-size: 1.15rem;
            line-height: 1.7;
            color: var(--text-secondary);
            max-width: 800px;
        }
        .highlight {
            color: var(--accent);
            font-weight: 600;
        }
        </style>
        
        <h1 class="about-header">About Me</h1>
        <p class="about-sub">
            I am a <span class="highlight">Data Scientist</span> at Capgemini (Client: Unilever) with over 2.5 years of experience building scalable ML systems. 
            My work sits at the intersection of <span class="highlight">Generative AI</span>, Data Engineering, and Product logic.
            <br><br>
            I don't just build models; I build end-to-end pipelines that solve real business problems. 
            Currently, I am deep-diving into Databricks, Agentic Workflows, and Production MLOps.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Interactive Cards Section
    # We wrap it in a container to ensure padding
    st.markdown('<div style="padding: 0 1rem;">', unsafe_allow_html=True)
    render_interactive_cards()
    st.markdown('</div>', unsafe_allow_html=True)
