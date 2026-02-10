import streamlit as st

# --------------------------------------------------
# 1. Page Config (MUST be the first command)
# --------------------------------------------------
st.set_page_config(
    page_title="Prajwal | Portfolio",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed" # Forces sidebar closed by default
)

# --------------------------------------------------
# 2. Imports
# --------------------------------------------------
# Page Imports
from src.ui.pages.home import render_home
from src.ui.pages.about import render_about
from src.ui.pages.career_snapshot import render_career_snapshot
from src.ui.pages.projects import render_projects
from src.ui.pages.resume import render_resume
from src.ui.pages.photography import render_photography

# Component Imports
from src.ui.components.navbar import render_navbar
from src.ui.components.footer import render_footer
from src.ui.chat.interface import render_chat_interface 

# Utility Imports (Theme Manager)
# NOTE: Ensure src/utils/theme.py exists with these functions
from src.ui.utils.theme import init_theme, load_theme_css


# --------------------------------------------------
# 3. Theme & Style Initialization
# --------------------------------------------------
# Initialize the session state for the theme (Light/Dark)
init_theme()

# Inject the dynamic CSS variables (Colors)
load_theme_css()

# Inject the static Layout/Typography styles (Spacing, Fonts)
def load_base_css():
    try:
        with open("src/ui/styles/base.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ CSS file not found: src/ui/styles/base.css")

load_base_css()


# --------------------------------------------------
# 4. State Management (Routing)
# --------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"


# --------------------------------------------------
# 5. Render Navbar
# --------------------------------------------------
# Renders the top navigation buttons and theme toggle
render_navbar()


# --------------------------------------------------
# 6. Main Content Router
# --------------------------------------------------
st.markdown('<div class="main-content">', unsafe_allow_html=True)

current_page = st.session_state.page

# Render the specific page content
if current_page == "Home":
    render_home()
elif current_page == "About":
    render_about()
elif current_page == "Career Snapshot":
    render_career_snapshot()
elif current_page == "Projects":
    render_projects()
elif current_page == "Resume":
    render_resume()
elif current_page == "Photography":
    render_photography()
elif current_page == "Ask Me":  # The dedicated page
    st.title("Ask Me Anything")
    render_chat_interface(key="page_chat_interface")

# --------------------------------------------------
# Global "Ask Me" Section
# --------------------------------------------------
# This will appear at the bottom of every page

st.markdown('</div>', unsafe_allow_html=True)


# --------------------------------------------------
# 7. Render Footer
# --------------------------------------------------
render_footer()
