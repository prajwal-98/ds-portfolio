import streamlit as st
from src.ui.components.projects_data import PROJECTS_DATA

def render_projects():
    """
    Renders the Projects Page.
    Structure:
    1. Header
    2. Hero Projects (Large Cards)
    3. Experiments Gallery (Horizontal Scroll)
    """
    
    # 1. Header
    st.markdown('<div style="margin-bottom: 60px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("""
        <h1 style="text-align: center;">Featured Work</h1>
        <p style="text-align: center; color: var(--text-secondary);">
            A selection of scalable systems and experiments.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Hero Projects Loop
    # We render each hero project as a distinct "Section"
    
    for project in PROJECTS_DATA["hero"]:
        with st.container():
            # Create a 2-column layout: Image (Left) vs Content (Right)
            # On mobile, this stacks naturally
            c1, c2 = st.columns([1, 1], gap="large")
            
            with c1:
                # Display Project Image
                st.image(project["image"], use_container_width=True)
            
            with c2:
                st.markdown(f"### {project['title']}")
                st.caption(project["tagline"])
                
                st.write(project["description"])
                
                # Tech Stack Badges
                tech_html = " ".join([f"<span style='background:var(--bg); padding:4px 8px; border-radius:4px; font-size:0.8rem; border:1px solid var(--line); margin-right:5px;'>{t}</span>" for t in project["tech_stack"]])
                st.markdown(f"<div style='margin: 15px 0;'>{tech_html}</div>", unsafe_allow_html=True)
                
                # Buttons
                b1, b2 = st.columns([1, 1.5])
                with b1:
                    st.button("🚀 Live Demo", key=f"btn_demo_{project['title']}", use_container_width=True)
                with b2:
                    st.button("💻 View Code", key=f"btn_code_{project['title']}", use_container_width=True)
            
            st.markdown("---") # Divider between projects

    # 3. Experiments Gallery (Grid)
    st.markdown("<h3 style='margin-top: 40px;'>🧪 Experiments & Snippets</h3>", unsafe_allow_html=True)
    
    # Grid Layout for smaller cards
    cols = st.columns(3)
    for i, exp in enumerate(PROJECTS_DATA["experiments"]):
        col = cols[i % 3] # Distribute across 3 columns
        with col:
            with st.container(border=True):
                st.markdown(f"**{exp['title']}**")
                st.caption(exp["desc"])
                # Small tags
                tags = " • ".join(exp["tags"])
                st.markdown(f"<small style='color:var(--accent);'>{tags}</small>", unsafe_allow_html=True)
