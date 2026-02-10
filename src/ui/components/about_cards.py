import streamlit as st

# --- MODAL CONTENT FUNCTIONS ---

@st.dialog("My Tech Stack")
def show_skills_modal():
    st.write("### Core Competencies")
    # Using columns for a grid layout of "icons" (text emojis for now, can be images later)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("**Languages**")
        st.write("🐍 Python, SQL, Bash")
    with c2:
        st.markdown("**GenAI & LLMs**")
        st.write("🤖 LangChain, RAG, OpenAI/Gemini APIs")
    with c3:
        st.markdown("**Data Eng**")
        st.write("🧱 Databricks, Spark, Airflow")
    
    st.write("---")
    st.caption("Focus: End-to-End System Design & Production ML")


@st.dialog("Photography & Creativity")
def show_photography_modal():
    st.markdown("### Beyond the Code")
    st.write("When I'm not architecting pipelines, I'm behind the lens.")
    st.write("I specialize in Street, Portrait, and Travel photography.")
    
    st.write("") # Spacer
    
    # The Gateway Button to the Full Page
    if st.button("📸 Enter Photography Gallery", use_container_width=True):
        st.session_state.page = "Photography" # We will build this page later
        st.rerun()


@st.dialog("Career Milestones")
def show_milestones_modal():
    st.markdown("### The Journey So Far")
    st.markdown("""
    - **2026 (Goal):** Transition to Product-Based GenAI Engineer Role
    - **2023 - Present:** Data Scientist @ Capgemini (Client: Unilever)
        - *Focus: Scalable GenAI Pipelines & Batch Inference*
    - **2022:** Graduated & Started Professional Career
    """)
    st.caption("Detailed timeline available in 'Career Snapshot' page.")


# --- MAIN RENDER FUNCTION ---

def render_interactive_cards():
    """
    Renders 3 interactive cards with 3D hover effects.
    """
    
    # 1. CSS for 3D Tilt Effect & Card Styling
    st.markdown("""
        <style>
        .about-card {
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s;
            cursor: pointer;
            height: 100%;
            position: relative;
        }
        
        .about-card:hover {
            transform: translateY(-8px);
            box-shadow: var(--card-shadow);
            border-color: var(--accent);
        }
        
        .card-icon {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            display: block;
        }
        
        .card-title {
            font-weight: 700;
            color: var(--text);
            margin-bottom: 0.5rem;
            display: block;
            font-size: 1.1rem;
        }
        
        .card-desc {
            font-size: 0.9rem;
            color: var(--text-secondary);
        }
        
        /* Mobile Stack Adjustment */
        @media (max-width: 768px) {
            .about-card { margin-bottom: 1rem; }
        }
        </style>
    """, unsafe_allow_html=True)

    # 2. Render Cards Grid
    # We use standard columns. The internal HTML gives the style.
    # The BUTTON is the interaction layer.
    
    c1, c2, c3 = st.columns(3)
    
    # --- CARD 1: SKILLS ---
    with c1:
        st.markdown("""
            <div class="about-card">
                <span class="card-icon">⚡</span>
                <span class="card-title">Skills & Stack</span>
                <span class="card-desc">Python, GenAI, Databricks, SQL</span>
            </div>
        """, unsafe_allow_html=True)
        # Invisible full-width button hack or just a standard button below
        if st.button("View Tech Stack", key="btn_about_skills", use_container_width=True):
            show_skills_modal()

    # --- CARD 2: PHOTOGRAPHY ---
    with c2:
        st.markdown("""
            <div class="about-card">
                <span class="card-icon">📸</span>
                <span class="card-title">Photography</span>
                <span class="card-desc">Street, Portrait & Travel</span>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Gallery Info", key="btn_about_photo", use_container_width=True):
            show_photography_modal()

    # --- CARD 3: MILESTONES ---
    with c3:
        st.markdown("""
            <div class="about-card">
                <span class="card-icon">🚀</span>
                <span class="card-title">Milestones</span>
                <span class="card-desc">My professional timeline</span>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Journey", key="btn_about_miles", use_container_width=True):
            show_milestones_modal()
