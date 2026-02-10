import streamlit as st

def render_career_preview():
    """
    Renders a preview of the Career Snapshot page.
    Currently shows the latest role as a clickable action.
    """
    
    # 1. Component CSS
    st.markdown("""
        <style>
        .career-section-header {
            margin-bottom: 1rem;
            color: var(--text);
            font-weight: 600;
        }
        
        /* Optional: We can style the specific button if we target it by key later,
           but standard Streamlit buttons work best for reliable clicking. */
        </style>
    """, unsafe_allow_html=True)

    # 2. Layout Container
    st.markdown('<div style="margin-bottom: 80px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("<h3 class='career-section-header'>Career Snapshot</h3>", unsafe_allow_html=True)
    
    # 3. The Interactive "Card" (Button)
    # We use a button because it handles the Python click event natively and reliably.
    # Text is formatted to look like a summary.
    btn_label = (
        "📍 LATEST ROLE: Data Scientist @ Capgemini (Unilever)\n"
        "Focus: GenAI Pipelines, Prompt Engineering & Batch Inference\n"
        "2.5+ Years Experience • Click to view full timeline →"
    )
    
    if st.button(btn_label, key="career_preview_btn", use_container_width=True):
        st.session_state.page = "Career Snapshot"
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
