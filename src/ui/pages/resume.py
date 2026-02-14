import streamlit as st
import base64
import os

def render_resume():
    st.markdown('<div style="margin-bottom: 40px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("""
        <h1 style="text-align: center;">Resume</h1>
        <p style="text-align: center; color: var(--text-secondary);">
            Proven experience in building scalable Data Science & GenAI systems.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # --- DYNAMIC PATH LOGIC ---
    # This gets the directory where resume.py is, then goes up to the root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming your structure is: root/src/ui/pages/resume.py
    # We go up 3 levels to reach the root, then into assets
    resume_path = os.path.join(current_dir, "../../../assets/resume.pdf")
    
    # Debug: If it fails, this will tell you exactly WHERE it is looking
    if not os.path.exists(resume_path):
        st.error(f"⚠️ File not found at: {resume_path}")
        st.info("Check if your folder is named 'assets' (lowercase) in GitHub!")
        return

    with open(resume_path, "rb") as f:
        pdf_data = f.read()
        b64_pdf = base64.b64encode(pdf_data).decode('utf-8')

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
    
    st.write("") 

    # PDF Preview
    pdf_display = f'<iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="1000" type="application/pdf" style="border:none;"></iframe>'
    st.markdown("### Preview")
    st.markdown(pdf_display, unsafe_allow_html=True)