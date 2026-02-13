import streamlit as st
import base64
import os

# --- 1. POP-UP DIALOG FUNCTIONS ---

@st.dialog("🏆 Hall of Fame", width="large")
def show_achievements():
    # --- CSS: ULTRA-WIDE & CARD STYLING ---
    st.markdown("""
    <style>
        /* 1. MAKE IT WIDE (Same as Photography Gallery) */
        div[data-testid="stDialog"] div[role="dialog"] {
            max-width: 95vw !important;
            padding: 20px !important;
        }

        /* 2. CARD STYLING */
        .trophy-card {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 0px; /* Margins handled by grid */
            height: 100%;       /* Forces equal height in row */
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            transition: transform 0.2s;
        }
        
        .trophy-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        }

        /* --- PROFESSIONAL COLORS --- */
        .trophy-gold   { border-left: 4px solid #FFD700; background: linear-gradient(to bottom right, #fffdf0, #fff); }
        .trophy-teal   { border-left: 4px solid #008080; }
        .trophy-blue   { border-left: 4px solid #3b82f6; }
        .trophy-purple { border-left: 4px solid #8b5cf6; }
        .trophy-dark   { border-left: 4px solid #334155; }

        /* --- PERSONAL COLORS --- */
        .trophy-crimson { border-left: 4px solid #e11d48; } /* Karate */
        .trophy-indigo  { border-left: 4px solid #6366f1; } /* NCC */
        .trophy-emerald { border-left: 4px solid #10b981; } /* Cricket */
        .trophy-orange  { border-left: 4px solid #f97316; } /* Hobby 4 */
        .trophy-cyan    { border-left: 4px solid #06b6d4; } /* Hobby 5 */

        /* TYPOGRAPHY */
        .trophy-title {
            font-weight: 800;
            font-size: 1rem;
            color: #1e293b;
            margin-bottom: 10px;
            min-height: 40px; /* Aligns titles */
            display: flex;
            align-items: center;
        }

        .trophy-desc {
            font-size: 0.85rem;
            color: #475569;
            line-height: 1.4;
        }
        
        .section-label {
            font-size: 1.2rem;
            font-weight: 800;
            color: #1e293b;
            margin-top: 10px;
            margin-bottom: 20px;
            border-bottom: 2px solid #f1f5f9;
            padding-bottom: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # 1. PROFESSIONAL IMPACT (5 CARDS)
    # ==========================================
    st.markdown('<div class="section-label">💼 Professional Impact</div>', unsafe_allow_html=True)
    
    c1, c2, c3, c4, c5 = st.columns(5)

    with c1: # AWARD
        st.markdown("""
        <div class="trophy-card trophy-gold">
            <div class="trophy-title">🏆 2x Best Employee</div>
            <div class="trophy-desc">
                Recipient of the top award at <b>Capgemini</b> twice. Recognized for critical delivery under pressure.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2: # SCALE
        st.markdown("""
        <div class="trophy-card trophy-teal">
            <div class="trophy-title">🚀 The Scale (Unilever)</div>
            <div class="trophy-desc">
                Engineered pipelines handling <b>10TB+ daily</b>. Optimized Spark jobs reducing costs by <b>40%</b>.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3: # CERTS
        st.markdown("""
        <div class="trophy-card trophy-blue">
            <div class="trophy-title">📜 Certified Expert</div>
            <div class="trophy-desc">
                • Azure Data Scientist<br>
                • Databricks Data Engineer<br>
                • Validated technical depth.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c4: # DUMMY 1
        st.markdown("""
        <div class="trophy-card trophy-purple">
            <div class="trophy-title">🧠 GenAI Architect</div>
            <div class="trophy-desc">
                Designed RAG systems for internal knowledge base, reducing search time by 60%. (Placeholder)
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c5: # DUMMY 2
        st.markdown("""
        <div class="trophy-card trophy-dark">
            <div class="trophy-title">⚡ Tech Lead</div>
            <div class="trophy-desc">
                Mentored a team of 5 junior developers, establishing best practices in Python & SQL. (Placeholder)
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ==========================================
    # 2. BEYOND THE CODE (With Spacing Fix & Popovers)
    # ==========================================
    st.markdown('<div class="section-label" style="margin-top: 40px;">⚡ Beyond the Code</div>', unsafe_allow_html=True)

    p1, p2, p3, p4, p5 = st.columns(5)

    # --- HELPER: Spacer to fix overlap ---
    def add_spacer():
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)

    # --- CARD 1: KARATE (Multiple Wins) ---
    with p1: 
        st.markdown("""
        <div class="trophy-card trophy-crimson">
            <div class="trophy-title">🥋 Karate Champion</div>
            <div class="trophy-desc">
                <b>Tournament Winner</b>. Cultivated discipline, focus, and the ability to perform under physical pressure.
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div style="height: 10px;"></div>', unsafe_allow_html=True)

        # MULTI-WIN POPOVER
        with st.popover("View Wins (3) 🥋", use_container_width=True):
            st.markdown("### 🥋 Tournament History")
            
            # TABS FOR CHRONOLOGY
            t_gold, t_silver, t_belt = st.tabs(["2021 Gold", "2019 Silver", "Black Belt"])
            
            with t_gold:
                st.info("🥇 State Championship - 1st Place (Kumite)")
                st.image("https://ui-avatars.com/api/?name=Gold&background=ffd700&color=000&size=400")
            
            with t_silver:
                st.warning("🥈 National Qualifiers - 2nd Place")
                st.image("https://ui-avatars.com/api/?name=Silver&background=c0c0c0&color=000&size=400")

            with t_belt:
                st.success("oss! Dan Promotion Grading")
                st.image("https://ui-avatars.com/api/?name=Black+Belt&background=000&color=fff&size=400")

    # --- 2. NCC ---
    with p2: 
        st.markdown("""
        <div class="trophy-card trophy-indigo">
            <div class="trophy-title">🎖️ N.C.C.</div>
            <div class="trophy-desc">
                <b>'A' Certificate</b>. Trained in military discipline, leadership, and patriotic service.
            </div>
        </div>
        """, unsafe_allow_html=True)
        add_spacer()
        with st.popover("View Badge 🎖️", use_container_width=True):
            st.subheader("🇮🇳 National Cadet Corps")
            st.image("https://ui-avatars.com/api/?name=NCC&background=6366f1&color=fff&size=400")

    # --- 3. CRICKET ---
    with p3: 
        st.markdown("""
        <div class="trophy-card trophy-emerald">
            <div class="trophy-title">🏏 Cricket</div>
            <div class="trophy-desc">
                <b>Regional Player</b>. Represented the district team. Strategy and resilience.
            </div>
        </div>
        """, unsafe_allow_html=True)
        add_spacer()
        with st.popover("View Team 📸", use_container_width=True):
            st.subheader("🏏 District Finals")
            st.caption("Team Captain - 2021")
            st.image("https://ui-avatars.com/api/?name=Cricket&background=10b981&color=fff&size=400")

    # --- 4. MARATHON ---
    with p4: 
        st.markdown("""
        <div class="trophy-card trophy-orange">
            <div class="trophy-title">🏃 Runner</div>
            <div class="trophy-desc">
                <b>Half-Marathon</b>. Completed 21km runs. Building deep stamina for long coding sprints.
            </div>
        </div>
        """, unsafe_allow_html=True)
        add_spacer()
        with st.popover("View Medal 🏅", use_container_width=True):
            st.subheader("🏃 City Marathon")
            st.caption("Finisher Medal - Time: 2h 15m")
            st.image("https://ui-avatars.com/api/?name=Medal&background=f97316&color=fff&size=400")

    # --- 5. CHESS ---
    with p5: 
        st.markdown("""
        <div class="trophy-card trophy-cyan">
            <div class="trophy-title">♟️ Chess</div>
            <div class="trophy-desc">
                <b>Rated 1500+</b>. Applying strategic foresight from the board to system architecture.
            </div>
        </div>
        """, unsafe_allow_html=True)
        add_spacer()
        with st.popover("View Stats 📊", use_container_width=True):
            st.subheader("♟️ Chess.com Profile")
            st.caption("Peak Rating: 1542 | Rapid")
            st.image("https://ui-avatars.com/api/?name=Stats&background=06b6d4&color=fff&size=400")

@st.dialog("📸 Photography Gallery", width="large")
def show_gallery():
    # --- CSS: THE FREE-SIZE MASONRY WALL ---
    st.markdown("""
        <style>
        /* Edge-to-edge dialog */
        div[data-testid="stDialog"] div[role="dialog"] {
            max-width: 95vw !important;
            padding: 0px !important;
            background-color: #000 !important;
        }

        /* 2. CLOSE BUTTON STYLING (The Red Button) */
        div[data-testid="stDialog"] button[aria-label="Close"] {
            color: #ef4444 !important; /* Bright Red */
            background-color: rgba(239, 68, 68, 0.1) !important; /* Light Red BG */
            border-radius: 50%;
            transition: all 0.2s;
            margin-top: 10px; /* Slight adjustment for edge-to-edge dialogs */
            margin-right: 10px;
        }

        div[data-testid="stDialog"] button[aria-label="Close"]:hover {
            color: #ffffff !important;
            background-color: #ef4444 !important; /* Solid Red on Hover */
        }

        /* 3. MASONRY GRID */
            .masonry-wrapper {
            column-count: 4;
            column-gap: 0px;
            width: 100%;
            background-color: #000;
        }

        .masonry-item {
            display: inline-block;
            width: 100%;
            margin: 0;
            padding: 0;
            overflow: hidden;
        }

        .masonry-item img {
            width: 100%;
            height: auto;
            display: block;
            transition: transform 0.6s ease;
            cursor: crosshair;
        }

        .masonry-item img:hover {
            transform: scale(1.05);
            filter: brightness(1.1);
            z-index: 10;
        }

        @media (max-width: 1024px) { .masonry-wrapper { column-count: 3; } }
        @media (max-width: 600px) { .masonry-wrapper { column-count: 2; } }
        </style>
    """, unsafe_allow_html=True)

    # --- AUTO-LOADER LOGIC ---
    img_dir = "assets/photography"
    
    def get_b64(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()

    if os.path.exists(img_dir):
        valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')
        files = sorted([f for f in os.listdir(img_dir) if f.lower().endswith(valid_extensions)])
        
        if not files:
            st.warning("Drop some photos in `assets/photography`!")
            return

        gallery_html = '<div class="masonry-wrapper">'
        for f in files:
            img_path = os.path.join(img_dir, f)
            b64_data = get_b64(img_path)
            gallery_html += f'<div class="masonry-item"><img src="data:image/jpeg;base64,{b64_data}"></div>'
        gallery_html += '</div>'
        
        st.markdown(gallery_html, unsafe_allow_html=True)
    else:
        st.error(f"Directory not found: {img_dir}")

@st.dialog("🛠️ Technologies powering my architecture", width="large")
def show_toolkit():
    # --- DARK MODE CSS ---
    st.markdown("""
    <style>
        /* 1. DIALOG CONTAINER (Deep Dark Background) */
        div[data-testid="stDialog"] div[role="dialog"] {
            background-color: #020617 !important; /* Very Dark Slate */
            color: #e2e8f0 !important;
            border: 1px solid #1e293b;
            box-shadow: 0 0 50px rgba(0,0,0, 0.7);
        }

        /* 2. TITLE & CLOSE BUTTON STYLING (Scoped to this Dialog) */
        
        /* The Header Container */
        div[data-testid="stDialog"] header {
            background-color: transparent !important;
            border-bottom: 1px solid #1e293b;
        }

        /* The Title Text ("Technologies powering...") */
        div[data-testid="stDialog"] h2 {
            color: #22d3ee !important; /* Bright Cyan Neon */
            font-family: 'Courier New', monospace !important;
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 1.2rem !important;
        }

        /* The Close Button (X) */
        div[data-testid="stDialog"] button[aria-label="Close"] {
            color: #ef4444 !important; /* Bright Red */
            background-color: rgba(239, 68, 68, 0.1) !important; /* Light Red BG */
            border-radius: 50%;
            transition: all 0.2s;
        }

        div[data-testid="stDialog"] button[aria-label="Close"]:hover {
            color: #ffffff !important;
            background-color: #ef4444 !important; /* Solid Red on Hover */
        }

        /* 3. CARD STYLING */
        .stack-card {
            background-color: #1e293b; /* Slate 800 */
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
            height: 100%;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }
        
        .stack-card:hover {
            transform: translateY(-5px);
            border-color: #94a3b8; /* Light Grey Hover */
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }

        /* 4. SECTION HEADERS (Clean White) */
        .stack-header {
            font-size: 0.95rem;
            font-weight: 800;
            color: #f1f5f9; /* White-ish */
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            border-bottom: 2px solid #334155;
            padding-bottom: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* 5. BADGE GRID */
        .badge-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }
        
        .badge-grid img {
            height: 28px;
            border-radius: 4px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        }
    </style>
    """, unsafe_allow_html=True)

    # --- ROW 1: GEN AI & DEEP LEARNING ---
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="stack-card">
            <div class="stack-header">🧠 Generative AI & LLMs</div>
            <div class="badge-grid">
                <img src="https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white">
                <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=chainlink&logoColor=white">
                <img src="https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black">
                <img src="https://img.shields.io/badge/LlamaIndex-white?style=for-the-badge&logo=alpaca&logoColor=black">
                <img src="https://img.shields.io/badge/Pinecone-black?style=for-the-badge&logo=pinecone&logoColor=white">
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="stack-card">
            <div class="stack-header">🕸️ Deep Learning</div>
            <div class="badge-grid">
                <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white">
                <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white">
                <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white">
                <img src="https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- ROW 2: ML & VIZ ---
    c3, c4 = st.columns(2)

    with c3:
        st.markdown("""
        <div class="stack-card">
            <div class="stack-header">🤖 Classical ML</div>
            <div class="badge-grid">
                <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
                <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white">
                <img src="https://img.shields.io/badge/numpy-013243?style=for-the-badge&logo=numpy&logoColor=white">
                <img src="https://img.shields.io/badge/XGBoost-EB4C4C?style=for-the-badge&logo=xgboost&logoColor=white">
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class="stack-card">
            <div class="stack-header">📊 Data Visualization</div>
            <div class="badge-grid">
                <img src="https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white">
                <img src="https://img.shields.io/badge/Matplotlib-3F4F75?style=for-the-badge&logo=python&logoColor=white">
                <img src="https://img.shields.io/badge/Seaborn-77ACF1?style=for-the-badge&logo=python&logoColor=white">
                <img src="https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white">
                <img src="https://img.shields.io/badge/PowerBI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black">
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- ROW 3: TOOLS ---
    st.markdown("""
    <div class="stack-card">
        <div class="stack-header">🛠️ Platforms & DevOps</div>
        <div class="badge-grid">
            <img src="https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white">
            <img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
            <img src="https://img.shields.io/badge/Visual%20Studio%20Code-0078d7?style=for-the-badge&logo=visual-studio-code&logoColor=white">
            <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
            <img src="https://img.shields.io/badge/Azure-0078D4?style=for-the-badge&logo=microsoft-azure&logoColor=white">
            <img src="https://img.shields.io/badge/Apache%20Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white">
        </div>
    </div>
    """, unsafe_allow_html=True)


# --- 2. MAIN RENDER FUNCTION ---

def render_interactive_cards():
    """
    Renders 3 cards.
    INCLUDES:
    1. Text Lift: Pulls the 'I architect...' header up.
    2. Card Lift: Pulls the cards up to meet the text.
    """
    
    st.markdown("""
        <style>
        /* 1. TEXT LIFT (The "Header Pull") */
        /* Targets the main H1 title ("I architect...") and pulls it up */
        h1 {
            padding-top: 0px !important;
            margin-top: -75px !important; /* Change this to -60px or -40px to tune it */
        }
        
        /* 2. CARD LIFT (The "Gap Fix") */
        /* Pulls the card container up to meet the text */
        div[data-testid="stHorizontalBlock"]:has(.tech-card) {
            margin-top: -80px !important;
        }

        /* 3. BASE CARD STYLING & UNIFIED GRADIENT */
        .tech-card {
            background: linear-gradient(135deg, #ffffff 0%, #e0f2f1 100%); 
            border: 1px solid rgba(0, 128, 128, 0.1);
            border-radius: 12px;
            padding: 25px 20px;
            text-align: left;
            transition: all 0.3s ease;
            height: 100%;
            position: relative;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 4px solid transparent; 
        }
        
        /* HOVER EFFECT */
        .tech-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            border-left: 4px solid #008080; /* Strong Teal Accent */
            filter: brightness(0.98);
        }

        /* 4. TYPOGRAPHY */
        .pillar-icon { font-size: 2rem; margin-bottom: 15px; display: block; }
        .pillar-title { font-size: 1.1rem; font-weight: 700; color: #1e293b; margin-bottom: 8px; display: block; }
        .pillar-desc { font-size: 0.9rem; color: #475569; line-height: 1.5; display: block; min-height: 60px; }

        /* 5. IMPACT BADGE */
        .impact-badge {
            background-color: rgba(0, 128, 128, 0.1);
            color: #008080;
            padding: 5px 10px;
            border-radius: 6px;
            font-size: 0.75rem;
            font-weight: 600;
            display: inline-block;
            margin-top: 15px;
            border: 1px solid rgba(0, 128, 128, 0.2);
        }

        /* 6. BUTTON STYLING */
        div[data-testid="stHorizontalBlock"]:has(.tech-card) .stButton button {
            background-color: #f3f4f6 !important;
            border: 1px solid #d1d5db !important;
            color: #374151 !important;
            width: 100% !important;
            border-radius: 8px !important;
            padding: 6px 0 !important;   
            min-height: 0px !important;  
            height: auto !important;
            margin-top: 15px !important;
            text-transform: uppercase !important;
            letter-spacing: 1.5px !important;
            font-weight: 700 !important;
            font-size: 0.75rem !important;
        }

        div[data-testid="stHorizontalBlock"]:has(.tech-card) .stButton button:hover {
            background-color: #008080 !important;
            color: #ffffff !important;
            border-color: #008080 !important;
        }

        </style>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    # --- CARD 1 ---
    with c1:
        st.markdown("""
            <div class="tech-card">
                <span class="pillar-icon">🏆</span>
                <span class="pillar-title">Milestones & Wins</span>
                <span class="pillar-desc">Track record of excellence at Capgemini and Unilever.</span>
                <div class="impact-badge">✨ 2x Award Winner & Certified DS</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("View Awards", key="btn_achv", use_container_width=True):
             show_achievements()

    # --- CARD 2 ---
    with c2:
        st.markdown("""
            <div class="tech-card">
                <span class="pillar-icon">📸</span>
                <span class="pillar-title">The Visual Eye</span>
                <span class="pillar-desc">Street and travel photography: finding patterns in chaos.</span>
                <div class="impact-badge">🎨 Street • Portrait • Travel</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Enter Gallery", key="btn_phot", use_container_width=True):
             show_gallery()

    # --- CARD 3 ---
    with c3:
        st.markdown("""
            <div class="tech-card">
                <span class="pillar-icon">🛠️</span>
                <span class="pillar-title">My Toolkit</span>
                <span class="pillar-desc">Orchestrating GenAI and Data Engineering systems.</span>
                <div class="impact-badge">⚡ Python • GenAI • Databricks</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("Inspect Stack", key="btn_tlkt", use_container_width=True):
             show_toolkit()