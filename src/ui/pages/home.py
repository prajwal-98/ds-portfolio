import streamlit as st
from src.ui.chat.interface import render_chat_interface

# --- 1. HERO SECTION ---
def render_hero():
    st.write("") 
    with st.container():
        c_text, c_img = st.columns([1.6, 1], gap="large")
        
        with c_text:
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
            
            b1, b2 = st.columns([0.4, 0.6])
            with b1:
                if st.button("Contact Me", type="primary", use_container_width=True):
                    st.markdown("[Go to Footer](#contact)") # Simple anchor link
            with b2:
                if st.button("Download Resume ⇩", use_container_width=True):
                    st.session_state.page = "Resume"
                    st.rerun()

        with c_img:
            # Replace with your image
            st.image("https://placehold.co/400x400/png?text=Prajwal", width=350) 

# --- 2. SKILLS SECTION ---
def render_skills():
    st.write("")
    st.divider()
    st.subheader("🚀 Technical Skills")
    
    # Simple columnar layout for skills
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("**Languages**")
        st.caption("Python, SQL, Bash")
    with c2:
        st.markdown("**GenAI**")
        st.caption("LangChain, RAG, OpenAI API")
    with c3:
        st.markdown("**Data Eng**")
        st.caption("PySpark, Databricks, ETL")
    with c4:
        st.markdown("**Tools**")
        st.caption("Git, Docker, Streamlit")

# --- 3. ASK ME ANYTHING (Chat Section) ---
def render_ask_maggie_section():
    st.write("")
    st.divider()
    st.subheader("🤖 Ask Me Anything")
    st.caption("Curious about my work? Chat with my AI agent below.")

    # We use a container to visually frame the chat in the middle of the page
    with st.container(border=True):
        # Unique key ensures this specific instance works correctly
        render_chat_interface(key="home_middle_chat")

# --- 4. PROJECTS SECTION (Preview) ---
def render_projects_preview():
    st.write("")
    st.divider()
    st.subheader("🛠️ Featured Projects")
    
    c1, c2 = st.columns(2)
    with c1:
        st.info("**GenAI Portfolio (This App)**\n\nBuilt a RAG-based portfolio using Streamlit & LangChain.")
    with c2:
        st.success("**Enterprise Data Pipeline**\n\nProcessed 1TB+ data using PySpark & Databricks.")
    
    if st.button("View All Projects →"):
        st.session_state.page = "Projects"
        st.rerun()

# --- 5. CAREER SNAPSHOT ---
def render_career_snapshot():
    st.write("")
    st.divider()
    st.subheader("📈 Career Snapshot")
    
    st.markdown("""
    * **Senior Data Scientist** @ Capgemini (2023 - Present)
    * **Data Analyst** @ StartUp Inc (2021 - 2023)
    """)

# --- 6. FOOTER (Contact) ---
def render_footer():
    st.write("")
    st.divider()
    st.subheader("📬 Get In Touch")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("📧 **Email:** prajwal@example.com")
    with c2:
        st.markdown("🔗 **LinkedIn:** [linkedin.com/in/prajwal](#)")
    with c3:
        st.markdown("🐙 **GitHub:** [github.com/prajwal](#)")
        
    st.write("")
    st.caption("© 2026 Prajwal. Built with Streamlit & Gemini.")

# --- MAIN PAGE ASSEMBLER ---
def render_home():
    # 1. Top: Hero
    render_hero()
    
    # 2. Next: Skills
    render_skills()
    
    # 3. Next: Ask Me Anything (Middle of page)
    render_ask_maggie_section()
    
    # 4. Next: Projects
    render_projects_preview()
    
    # 5. Next: Career Snapshot
    render_career_snapshot()
    
    # 6. Bottom: Footer
    render_footer()