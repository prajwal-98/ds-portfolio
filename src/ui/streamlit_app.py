# SRC/UI/StreamlitApp.py
import streamlit as st
from components import hero_slider

st.set_page_config(layout="wide", page_title="DS Portfolio")

# global small CSS to reduce Streamlit padding and help centering
st.markdown(
    """
    <style>
    .main > div.block-container { padding-left: 18px; padding-right: 18px; }
    </style>
    """,
    unsafe_allow_html=True,
)

def get_projects():
    # replace with your real project objects / read from a config or JSON
    return [
        {
            "title": "Ecom Reviews Explorer",
            "subtitle": "Filter by market, brand, category — review insights & charts",
            "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1200&q=80",
            "link": "https://your-app-link/project1"
        },
        {
            "title": "LLM Format Tagging",
            "subtitle": "Efficient batching & token-optimised prompts",
            "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=1200&q=80",
            "link": "https://your-app-link/project2"
        },
        {
            "title": "Analytics Dashboard",
            "subtitle": "Live charts: avg ratings, rating trend, brand compare",
            "image": "https://images.unsplash.com/photo-1508385082359-f9c3e4b1e33b?w=1200&q=80",
            "link": "https://your-app-link/project3"
        }
    ]

def main():
    st.header("Portfolio — Hero")
    projects = get_projects()
    hero_slider(projects, height=400)

    # rest of the app...
    st.markdown("---")
    st.subheader("Other sections")
    st.write("Put your project cards, charts and details below.")

if __name__ == "__main__":
    main()