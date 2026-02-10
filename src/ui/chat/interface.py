import streamlit as st

def render_chat_interface(location="default"):
    """
    Renders the Chat Interface with the Premium 'Card' Design.
    Args:
        location (str): Unique ID ('modal' or 'home_section') to fix duplicate key errors.
    """
    # 1. Initialize History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # 2. Chat Container
    # We use a container without a border so the internal HTML card defines the look
    chat_container = st.container(height=450)
    
    with chat_container:
        # --- STATE 1: EMPTY (The Premium Card Look) ---
        if not st.session_state.messages:
            # IMPORTANT: This HTML block is FLUSH LEFT (No spaces at start) 
            # to prevent it from showing as raw code.
            st.markdown("""
<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100%; text-align: center; padding-top: 20px;">
    <div style="background-color: #E6F3F5; color: #0E5A65; padding: 6px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); text-transform: uppercase;">
        ✨ Ask Maggie
    </div>
    <h2 style="font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-weight: 700; color: #1a1a1a; font-size: 2rem; margin-bottom: 10px; letter-spacing: -0.02em;">
        Curious about my experience?
    </h2>
    <p style="color: #666; font-size: 1.1rem; line-height: 1.6; max-width: 550px; margin: 0 auto;">
        I'm an LLM-powered assistant. Ask me about my <b>GenAI projects</b>, <b>tech stack</b>, or request simple code snippets.
    </p>
</div>
""", unsafe_allow_html=True)
            
        # --- STATE 2: ACTIVE (Chat Bubbles) ---
        else:
            for msg in st.session_state.messages:
                st.chat_message(msg["role"]).write(msg["content"])

    # 3. Input Area (Unique Key Fix)
    unique_key = f"chat_input_{location}"
    
    if prompt := st.chat_input("Ask Maggie anything...", key=unique_key):
        # User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Dummy AI Response
        response = f"I noticed you asked: '{prompt}'. (Backend connection coming soon!)"
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
