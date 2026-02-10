import streamlit as st

def render_hero():
    st.markdown("""
        <style>
        .hero-title {
            font-size: 3.5rem;
            font-weight: 800;
            line-height: 1.1;
            background: linear-gradient(135deg, var(--text) 0%, var(--text-secondary) 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            margin-bottom: 1.5rem;
        }
        .hero-subtitle {
            font-size: 1.2rem;
            color: var(--text-secondary);
            text-align: center;
            max-width: 700px;
            margin: 0 auto 2rem auto;
            line-height: 1.6;
        }
        </style>
        <div style="margin-bottom: 80px; padding: 0 1rem;">
            <h1 class="hero-title">
                Data Science | Machine Learning<br>GenAI | Python
            </h1>
            <p class="hero-subtitle">
                Building scalable Data Science and Generative AI solutions from 
                <span style="color: var(--accent); font-weight:600;">idea</span> → 
                <span style="color: var(--accent); font-weight:600;">architecture</span> → 
                <span style="color: var(--accent); font-weight:600;">deployment</span>.
            </p>
        </div>
    """, unsafe_allow_html=True)
