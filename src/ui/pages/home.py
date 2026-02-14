import streamlit as st
import base64
import os
from PIL import Image
import io

@st.dialog("🤖 Ask Prajwal's AI Assistant")
def open_ask_me_dialog():
    st.write("I have read Prajwal's resume and codebase. Ask me anything!")
    user_query = st.chat_input("Ex: What is your experience with RAG?")
    if user_query:
        with st.chat_message("user"):
            st.write(user_query)
        with st.chat_message("assistant"):
            st.write("I am a demo bot. Connect your logic here to answer: " + user_query)

def get_image_base64(path):
    if os.path.exists(path):
        try:
            img = Image.open(path)
            width, height = img.size
            # Keep crop logic
            img = img.crop((0, height * 0.1, width, height * 0.9)) 
            
            buffered = io.BytesIO()
            img.save(buffered, format="JPEG")
            return base64.b64encode(buffered.getvalue()).decode()
        except Exception as e:
            st.error(f"Error processing image: {e}")
            return None
    return None

def render_home():
    # --- 1. LOCAL STYLES ---
    st.markdown("""
        <style>
            /* --- TEXT STYLING --- */
            .hero-name-text {
                font-size: 2.5rem !important;
                font-weight: 800 !important;
                color: var(--text) !important;
                line-height: 1.0 !important;
                margin-bottom: 5px !important;
                margin-left: 13px !important;
            }
            .hero-intro-text {
                font-size: 1rem !important;
                font-weight: 600 !important;
                color: var(--text) !important;
                margin-bottom: 0px !important;
                margin-left: 15px !important;
            }
            .hero-detail-text {
                font-size: 1rem !important;
                color: grey !important;
                font-weight: 400 !important;
                margin-top: 10px !important;
                margin-left: 15px !important;
            }

            /* --- IMAGE STYLING --- */
            .profile-pic-square {
                width: 350px !important;   
                height: 400px !important;  
                border-radius: 12px !important;
                object-fit: cover !important;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1) !important;
                margin-top: -20px !important;  
                margin-left: -40px !important;
                margin-bottom: 30px !important;  
            }

            /* --- NEW "CHAT INPUT" STYLE BUTTON --- */
            div.stButton > button[kind="primary"] {
                /* Make it look like a text box */
                background: white !important;
                color: #666 !important; /* Grey text like a placeholder */
                border: 1px solid #ddd !important;
                border-radius: 12px !important;
                
                /* Size & Spacing */
                padding: 12px 20px !important;
                width: 380px !important; /* Wider, like a search bar */
                margin-top: 25px !important; 
                margin-left: 100px !important; /* Matches your text padding */
                
                /* Text alignment */
                display: flex !important;
                justify-content: space-between !important; /* Text left, Icon right */
                align-items: center !important;
                
                font-size: 0.95rem !important;
                font-weight: 400 !important;
                box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
                transition: all 0.2s ease !important;
            }

            }
        </style>
    """, unsafe_allow_html=True)

    # 2. CONVERT YOUR PHOTO
    # img_path = r"D:/ds-portfolio/assets/profile_pic/U89A0267.JPG"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    img_path = os.path.normpath(os.path.join(current_dir, "../../../assets/profile_pic/U89A0267.JPG"))

    img_base64 = get_image_base64(img_path)
    
    # Fallback to a placeholder if file is missing
    display_img = f"data:image/JPG;base64,{img_base64}" if img_base64 else "https://ui-avatars.com/api/?name=Prajwal"

    # --- 2. THE LAYOUT ---
    col_text, col_img = st.columns([1.5, 1], gap="small", vertical_alignment="center")

    # --- LEFT COLUMN ---
    with col_text:
        # 1. TEXT SECTION
        st.markdown("""
            <div style="text-align: left; margin-top: -60px; padding-left: 100px;"> 
                <span class="hero-intro-text">I am</span><br>
                <span class="hero-name-text">Prajwal Acharya</span><br>
                <span class="hero-detail-text">
                    <span style="font-size: 0.9rem; opacity: 0.8;">I design, code and build. Inspired by tough problems</span>
                </span>
            </div>
        """, unsafe_allow_html=True)
        
        # 2. BUTTON SECTION (The Chat Bar)
        # We use spaces in the label to push the sparkle icon to the far right
        if st.button("Ask Maggie to analyze my resume ✨", type="primary"):
            open_ask_me_dialog()
    
    

    # --- RIGHT COLUMN ---
    with col_img:
        st.markdown(f"""
            <div style="display: flex; justify-content: center;">
                <img src="{display_img}" 
                     class="profile-pic-square">
            </div>
        """, unsafe_allow_html=True)