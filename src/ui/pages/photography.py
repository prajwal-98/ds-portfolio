import streamlit as st

def render_photography():
    """
    Renders the Photography Portfolio.
    Hidden from main nav, accessed via About Page or Footer.
    """
    
    # 1. Header with "Back" Navigation
    st.markdown('<div style="margin-bottom: 40px; padding: 0 1rem;">', unsafe_allow_html=True)
    
    # A small "Back to Home" button for good UX since there is no nav link
    if st.button("← Back to Home", key="photo_back_btn"):
        st.session_state.page = "Home"
        st.rerun()
        
    st.markdown("""
        <h1 style="text-align: center; margin-top: 20px;">Visual Stories</h1>
        <p style="text-align: center; color: var(--text-secondary);">
            Capturing moments between the lines of code.
        </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Gallery CSS (Masonry-ish feel)
    st.markdown("""
        <style>
        .photo-card {
            border-radius: 12px;
            overflow: hidden;
            margin-bottom: 20px;
            transition: transform 0.2s;
        }
        .photo-card:hover {
            transform: scale(1.02);
            box-shadow: var(--card-shadow);
        }
        img {
            width: 100%;
            height: auto;
            display: block;
            border-radius: 12px;
        }
        </style>
    """, unsafe_allow_html=True)

    # 3. Category Tabs
    tab1, tab2, tab3 = st.tabs(["🏙️ Street", "🏔️ Travel", "👤 Portrait"])

    # Helper to render a grid of images
    def render_grid(images):
        c1, c2, c3 = st.columns(3)
        for i, img_url in enumerate(images):
            # Distribute images across 3 columns
            with [c1, c2, c3][i % 3]:
                st.markdown(f"""
                    <div class="photo-card">
                        <img src="{img_url}" loading="lazy">
                    </div>
                """, unsafe_allow_html=True)

    # --- TAB 1: STREET ---
    with tab1:
        render_grid([
            "https://images.unsplash.com/photo-1517457373958-b7bdd4587205?w=800&q=80",
            "https://images.unsplash.com/photo-1476900966801-41e1518f88a9?w=800&q=80",
            "https://images.unsplash.com/photo-1444723121867-c61208252060?w=800&q=80"
        ])

    # --- TAB 2: TRAVEL ---
    with tab2:
        render_grid([
            "https://images.unsplash.com/photo-1476514525535-07fb3b4ae5f1?w=800&q=80",
            "https://images.unsplash.com/photo-1501785888041-af3ef285b470?w=800&q=80",
            "https://images.unsplash.com/photo-1504609773096-104ff10587bd?w=800&q=80"
        ])

    # --- TAB 3: PORTRAIT ---
    with tab3:
        st.info("📸 Portrait gallery coming soon...")

    # 4. Footer for this page
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("<div style='text-align: center; color: var(--text-tertiary);'>Shot on Sony Alpha / iPhone</div>", unsafe_allow_html=True)
