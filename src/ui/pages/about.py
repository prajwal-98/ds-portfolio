import streamlit as st
from src.ui.components.about_cards import render_interactive_cards

def render_about():
    # 1. THE POWER INTRO
    st.markdown('<div style="margin-top: 30px; margin-bottom: 55px; padding: 0 1rem;">', unsafe_allow_html=True)
    
    st.markdown("""
        <style>
        .power-header {
            font-size: 2.8rem !important; 
            font-weight: 700 !important;
            color: var(--text) !important;
            letter-spacing: -2px !important;
            line-height: 1 !important;
            margin-bottom: 0px !important; 
            padding-bottom: 0px !important;
            margin-left: 40px !important;
        }
        
        .power-sub {
            font-size: 1rem !important; 
            line-height: 1.5 !important;
            color: var(--text-secondary) !important;
            font-weight: 500 !important; 
            max-width: 900px;
            margin-left: 40px !important;
            /* TIGHTENS THE GAP TO THE TITLE */
            margin-top: -5px !important; 
            padding-top: 0px !important;
        }
        
        .highlight-teal {
            color: #008080 !important;
            font-weight: 600 !important;
        }
        </style>
        
        <h1 class="power-header">Code. Impact. <span class="highlight-teal">Perspective.</span></h1>
        
        <p class="power-sub">
            I engineer intelligence—bridging the gap between abstract research and production reality with a creative eye for patterns.
        </p>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. THE CARDS
    st.markdown('<div style="padding: 0 1rem; margin-bottom: 60px;">', unsafe_allow_html=True)
    render_interactive_cards()
    st.markdown('</div>', unsafe_allow_html=True)

    # # 3. FOOTER
    # st.divider()
    # st.caption("Currently deep-diving into Agentic Workflows & Databricks.")