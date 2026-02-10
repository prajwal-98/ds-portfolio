import streamlit as st

def init_theme():
    """Initialize theme state if not present."""
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "light" 

def toggle_theme_mode():
    """Switches between light and dark mode."""
    if st.session_state.theme_mode == "dark":
        st.session_state.theme_mode = "light"
    else:
        st.session_state.theme_mode = "dark"

def load_theme_css():
    """
    Injects the CSS variables based on the current session state.
    """
    mode = st.session_state.get("theme_mode", "light")
    
    if mode == "dark":
        # --- DARK MODE ---
        css = """
        <style>
            :root {
                --bg: #121212;              /* Pure Black/Grey */
                --surface: #1E1E1E;         /* Dark Grey */
                --surface-hover: #2C2C2C;
                --text: #E0E0E0;            /* Light Grey */
                --text-secondary: #A0A0A0;  
                --text-tertiary: #606060;
                --accent: #D4D4D4;          /* Silver Accent */
                --line: #333333;            
                --card-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.6);
            }
            .stApp { background-color: var(--bg); }
        </style>
        """
    else:
        # --- LIGHT MODE (STRICT WHITE/GREY GRADIENT) ---
        css = """
        <style>
            :root {
                /* STRICT MONOCHROME PALETTE */
                --surface: #FFFFFF;         /* Pure White Cards */
                --surface-hover: #F0F0F0;
                --text: #111111;            /* Almost Black */
                --text-secondary: #444444;  /* Dark Grey */
                --text-tertiary: #888888;   /* Light Grey */
                --accent: #666666;          /* Mid Grey Accent */
                --line: #D1D1D1;            /* Visible Grey Border */
                --card-shadow: 0 8px 16px rgba(0, 0, 0, 0.1); 
            }
            
            /* THE VISIBLE SILVER GRADIENT */
            .stApp { 
                /* Starts Pure White (Top Left) -> Ends Metallic Grey (Bottom Right) */
                background: linear-gradient(to bottom right, #FFFFFF 0%, #E6E6E6 100%) !important;
                background-attachment: fixed !important;
            }
        </style>
        """
    
    st.markdown(css, unsafe_allow_html=True)
