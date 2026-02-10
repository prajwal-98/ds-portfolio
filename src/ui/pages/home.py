import streamlit as st
from src.ui.chat.interface import render_chat_interface

# --- 1. POP-UP MODAL (Hero Button) ---
@st.dialog("Ask Maggie ✨", width="large")
def open_maggie_modal():
    # Pass 'modal' to generate a unique key
    render_chat_interface(location="modal")

# --- 2. HERO SECTION ---
def render_hero():
    st.write("") 
    with st.container():
        st.markdown('<div class="hero-container">', unsafe_allow_html=True)
        c_text, c_img = st.columns([1.6, 1], gap="large")
        
        with c_text:
            st.markdown('<div class="hero-text">', unsafe_allow_html=True)
            st.markdown("""
            <h1 style='margin-bottom: 0px;'>Prajwal</h1>
            <h3 style='font-weight: 400; color: #666; margin-top: 0px;'>Data Scientist</h3>
            <br>
            <p style='font-size: 1.2rem; line-height: 1.6;'>
                Data Scientist building <b>Machine Learning</b> and <b>Generative AI</b> systems end-to-end. 
                Focusing on scalable pipelines from idea to deployment.
            </p>
            """, unsafe_allow_html=True)
            
            st.write("") 
            
            b1, b2, spacer = st.columns([0.35, 0.45, 0.5])
            with b1:
                if st.button("About Me", type="primary", use_container_width=True):
                    st.session_state.page = "About"
                    st.rerun()
            with b2:
                # TRIGGERS THE POP-UP
                if st.button("Ask Maggie ✨", use_container_width=True):
                    open_maggie_modal()
            
            st.markdown('</div>', unsafe_allow_html=True)

        with c_img:
            st.markdown('<div class="hero-image-container">', unsafe_allow_html=True)
            st.image("https://placehold.co/400x400/png?text=Prajwal", width=350) 
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# --- 3. EMBEDDED ASK MAGGIE SECTION (Bottom of Home) ---
def render_ask_maggie_section():
    st.write("")
    st.write("")
    st.divider()
    
    # We wrap it in a bordered container to frame the "Card" nicely
    with st.container(border=True):
        # Pass 'home_section' to generate a unique key
        render_chat_interface(location="home_section")

# --- MAIN RENDER ---
def render_home():
    render_hero()
    # render_tech_stack()      <-- Uncomment when ready
    # render_featured_projects() <-- Uncomment when ready
    render_ask_maggie_section()
