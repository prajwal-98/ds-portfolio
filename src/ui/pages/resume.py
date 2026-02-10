import streamlit as st
import base64
import os

def render_resume():
    """
    Renders the Resume Page with a Download Button and PDF Preview.
    """
    
    # 1. Header
    st.markdown('<div style="margin-bottom: 40px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("""
        <h1 style="text-align: center;">Resume</h1>
        <p style="text-align: center; color: var(--text-secondary);">
            Proven experience in building scalable Data Science & GenAI systems.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. File Path Logic
    # We look for the file in 'assets/resume.pdf'
    # Adjust this path if your folder structure is different
    resume_path = "assets/resume.pdf"
    
    # Check if file exists to prevent crash
    if not os.path.exists(resume_path):
        st.error("⚠️ Resume file not found. Please place 'resume.pdf' in the 'assets' folder.")
        return

    # 3. Read File for Download & Display
    with open(resume_path, "rb") as f:
        pdf_data = f.read()
        b64_pdf = base64.b64encode(pdf_data).decode('utf-8')

    # 4. Download Button (Centered)
    # We use columns to center the button
    c1, c2, c3 = st.columns([1, 1, 1])
    with c2:
        st.download_button(
            label="📄 Download PDF Resume",
            data=pdf_data,
            file_name="Prajwal_DataScientist_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
    
    st.write("") # Spacer

    # 5. PDF Preview (Iframe)
    # This embeds the PDF directly in the browser
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
    
    st.markdown("### Preview")
    st.markdown(pdf_display, unsafe_allow_html=True)
