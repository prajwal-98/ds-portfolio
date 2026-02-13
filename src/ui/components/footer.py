import streamlit as st

def render_footer():
    # 1. Load FontAwesome (This imports the icons)
    st.markdown(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">', 
        unsafe_allow_html=True
    )

    # 2. Render the Footer
    st.markdown("""
<style>
    .footer-container {
        width: 100%;
        background-color: transparent;
        padding: 15px 0;
        margin-top: 0px;
        text-align: center;
        border-top: 1px solid #eaeaea;
    }
    .social-links-row {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px;
        margin-bottom: 10px;
    }
    .social-icon {
        display: inline-flex;
        justify-content: center;
        align-items: center;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        border: 2px solid #333;
        color: #333 !important;
        font-size: 1.1rem;
        text-decoration: none;
        transition: all 0.3s ease;
        background: transparent;
    }
    .social-icon:hover {
        background-color: #008080;
        border-color: #008080;
        color: white !important;
        transform: translateY(-3px);
        box-shadow: 0 4px 10px rgba(0, 128, 128, 0.3);
    }
    .footer-text {
        color: #555;
        font-size: 0.8rem;
        font-weight: 400;
    }
</style>

<div class="footer-container">
    <div class="social-links-row">
        <a href="https://linkedin.com/" target="_blank" class="social-icon">
            <i class="fab fa-linkedin-in"></i>
        </a>
        <a href="https://github.com/" target="_blank" class="social-icon">
            <i class="fab fa-github"></i>
        </a>
        <a href="https://twitter.com/" target="_blank" class="social-icon">
            <i class="fab fa-twitter"></i>
        </a>
        <a href="https://instagram.com/" target="_blank" class="social-icon">
            <i class="fab fa-instagram"></i>
        </a>
        <a href="mailto:prajwal@example.com" class="social-icon">
            <i class="fas fa-envelope"></i>
        </a>
    </div>
    <div class="footer-text">
        © 2026 Prajwal Acharya.
    </div>
</div>
""", unsafe_allow_html=True)