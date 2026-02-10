import streamlit as st

def render_footer():
    """
    Renders a clean, horizontal footer at the bottom of the page.
    """
    
    # CSS for horizontal layout
    st.markdown("""
        <style>
        .footer-container {
            margin-top: 80px;
            padding-top: 30px;
            padding-bottom: 30px;
            border-top: 1px solid var(--line);
            text-align: center;
        }
        
        /* Flexbox to keep links in a row */
        .social-links-row {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 2rem; /* Spacing between links */
            margin-bottom: 1rem;
        }
        
        .social-link {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 1.1rem;
            font-weight: 500;
            transition: color 0.2s, transform 0.2s;
        }
        
        .social-link:hover {
            color: var(--accent);
            transform: translateY(-2px);
        }
        
        .footer-text {
            color: var(--text-tertiary);
            font-size: 0.85rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-container">', unsafe_allow_html=True)
    
    # 1. Social Links (Horizontal Row)
    st.markdown("""
        <div class="social-links-row">
            <a href="https://linkedin.com/" target="_blank" class="social-link">LinkedIn</a>
            <a href="https://github.com/" target="_blank" class="social-link">GitHub</a>
            <a href="mailto:prajwal@example.com" class="social-link">Email</a>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. Copyright Text
    st.markdown("""
        <div class="footer-text">
            © 2026 Prajwal. Built with Streamlit & Gemini.
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
