import streamlit as st

def render_maggie_assistant():
    st.markdown("""
        <style>
        .maggie-shell {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 24px;
            padding: 2rem;
            max-width: 800px;
            margin: 0 auto;
            box-shadow: var(--card-shadow);
            text-align: center;
        }
        .maggie-badge {
            background: rgba(14, 165, 165, 0.1);
            color: var(--accent);
            font-size: 0.75rem;
            font-weight: 700;
            padding: 6px 16px;
            border-radius: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-bottom: 80px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("""
        <div class="maggie-shell">
            <span class="maggie-badge">✨ Ask Maggie</span>
            <h3 style="margin-top: 1rem; margin-bottom: 0.5rem;">Curious about my experience?</h3>
            <p style="color: var(--text-tertiary); font-size: 0.95rem; margin-bottom: 1.5rem;">
                I'm an LLM-powered assistant. Ask me about my projects, tech stack, or simple code examples.
            </p>
    """, unsafe_allow_html=True)

    # Input Logic
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        query = st.chat_input("Ask Maggie anything...", key="home_maggie_input")
        if query:
            st.info(f"Maggie is thinking about: '{query}' (Backend connection pending...)")

    st.markdown('</div></div>', unsafe_allow_html=True)
