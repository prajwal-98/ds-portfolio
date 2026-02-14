import streamlit as st

# --- 1. CONFIGURATION ---
if __name__ == "__main__":
    st.set_page_config(
        page_title="Projects | Prajwal",
        page_icon="🧪",
        layout="wide"
    )

def render_dev_indicator():
    """Renders a small fixed 'STAGING' badge in the bottom right."""
    st.markdown("""
        <style>
        .dev-badge {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #f59e0b; /* Amber/Orange */
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 700;
            z-index: 9999;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            pointer-events: none;
        }
        </style>
        <div class="dev-badge">🚧 DEV MODE</div>
    """, unsafe_allow_html=True)

# --- 2. DATA: PROJECTS ---
PROJECTS = [
    {
        "title": "GenAI Portfolio Engine",
        "category": "GenAI",
        "tags": ["Streamlit", "LangChain", "RAG", "Pinecone"],
        "description": "A self-aware portfolio that uses RAG to answer questions about my resume and code.",
        "links": {"GitHub": "#", "Live Demo": "#"},
        "image": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "title": "Real-Time Fraud Guard",
        "category": "Data Engineering",
        "tags": ["PySpark", "Databricks", "Kafka", "MLflow"],
        "description": "Enterprise-grade pipeline processing 10TB+ daily transaction data.",
        "links": {"GitHub": "#"},
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "title": "Enterprise LLM Tagger",
        "category": "GenAI",
        "tags": ["Python", "OpenAI API", "AsyncIO"],
        "description": "Designed an async batch-processing system to tag 50k+ product descriptions.",
        "links": {"GitHub": "#"},
        "image": "https://images.unsplash.com/photo-1662947036643-2339bd9273c5?q=80&w=1000&auto=format&fit=crop"
    },
    {
        "title": "Legacy to Lakehouse Migration",
        "category": "Cloud Architecture",
        "tags": ["Azure", "Terraform", "Airflow"],
        "description": "Migrated on-prem SQL Server infrastructure to Azure Data Lake.",
        "links": {"GitHub": "#"},
        "image": "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=1000&auto=format&fit=crop"
    }
]

# --- 3. DATA: NOTEBOOKS ---
NOTEBOOKS = [
    {"name": "Churn Prediction", "tech": "XGBoost", "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80", "github": "#", "insight": "Achieved 89% accuracy."},
    {"name": "Movie Recommender", "tech": "SVD / Matrix Fac", "img": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=600&q=80", "github": "#", "insight": "Solved cold-start problem."},
    {"name": "Stock Forecasting", "tech": "LSTM / TensorFlow", "img": "https://images.unsplash.com/photo-1611974765270-ca1258634369?w=600&q=80", "github": "#", "insight": "Multi-layer LSTM model."},
    {"name": "Titanic EDA", "tech": "Seaborn", "img": "https://images.unsplash.com/photo-1524661135-423995f22d0b?w=600&q=80", "github": "#", "insight": "Visualized survival skew."},
    {"name": "Twitter Sentiment", "tech": "NLTK / VADER", "img": "https://images.unsplash.com/photo-1611605698389-377a032434f6?w=600&q=80", "github": "#", "insight": "Analyzed 50k tweets."},
    {"name": "Housing Prices", "tech": "Scikit-Learn", "img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600&q=80", "github": "#", "insight": "Regression analysis on Ames data."},
    {"name": "Image Classifier", "tech": "PyTorch / CNN", "img": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&q=80", "github": "#", "insight": "ResNet-50 on CIFAR-10."},
    {"name": "Credit Fraud", "tech": "Anomaly Detect", "img": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&q=80", "github": "#", "insight": "Detected fraud in imbalanced data."}
]

# --- 4. CSS STYLING ---
def load_project_css():
    st.markdown("""
    <style>
        .block-container { padding-top: 1rem !important; padding-bottom: 2rem !important; }
    
        /* --- 1. MAIN PROJECT CARD --- */
        .project-card {
            background-color: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
            height: 100%;
            display: flex; flex-direction: column; text-decoration: none;
        }
        .project-card:hover { transform: translateY(-6px); box-shadow: 0 12px 24px rgba(0,0,0,0.1); border-color: #38bdf8; }
        .card-img-box { height: 180px; width: 100%; overflow: hidden; position: relative; border-bottom: 1px solid #f1f5f9; }
        .card-img-box img { width: 100%; height: 100%; object-fit: cover; transition: transform 0.6s ease; }
        .project-card:hover .card-img-box img { transform: scale(1.08); }
        .card-body { padding: 20px; flex-grow: 1; display: flex; flex-direction: column; }
        .card-title { font-size: 1.15rem; font-weight: 700; color: #1e293b; margin-bottom: 8px; }
        .card-desc { font-size: 0.9rem; color: #64748b; line-height: 1.5; margin-bottom: 16px; flex-grow: 1; }
        .tech-pill { background-color: #f1f5f9; color: #475569; font-size: 0.75rem; font-weight: 600; padding: 4px 10px; border-radius: 20px; border: 1px solid #e2e8f0; }
        .badge-container { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
        .card-footer { display: flex; gap: 10px; margin-top: auto; }
        .btn-link { flex: 1; text-align: center; padding: 8px 0; border-radius: 6px; font-size: 0.85rem; font-weight: 600; text-decoration: none; transition: all 0.2s; }
        .btn-primary { background-color: #0f172a; color: #ffffff !important; }
        .btn-secondary { background-color: #ffffff; color: #0f172a !important; border: 1px solid #cbd5e1; }
        
        /* --- 2. NOTEBOOK SPECIFIC STYLING --- */
        .nb-tech-green {
            color: #22c55e !important;
            font-size: 0.85rem;
            font-weight: 600;
            margin-top: 2px;
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        /* Targets ONLY the buttons in the notebook grid containers */
        div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] button {
            background-color: #ffffff !important;
            color: #1e293b !important;
            border: 1px solid #cbd5e1 !important;
            border-radius: 8px !important;
            padding: 10px 40px !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }

        div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] button:hover {
            border-color: #22c55e !important;
            background-color: #f8fafc !important;
        }
    </style>
    """, unsafe_allow_html=True)

# --- 5. DIALOG: INSIGHT POPUP ---
@st.dialog("📄 Notebook Details", width="large")
def show_notebook_popup(nb):
    c1, c2 = st.columns([1, 2], gap="medium")
    with c1:
        st.image(nb['img'], use_container_width=True)
    with c2:
        st.markdown(f"## {nb['name']}")
        st.markdown(f"<span style='color:#22c55e; font-weight:700;'>🔧 {nb['tech']}</span>", unsafe_allow_html=True)
        st.info(nb.get('insight', 'No summary available.'))
        st.link_button("View Source Code on GitHub ↗", nb.get('github', '#'), type="primary", use_container_width=True)
    st.divider()
    st.markdown("### 🔍 Technical Overview")
    st.write("This notebook explores data patterns using advanced statistical methods.")

# --- 6. RENDERERS ---

def render_project_card(project):
    badges_html = "".join([f'<span class="tech-pill">{tag}</span>' for tag in project["tags"]])
    buttons_html = ""
    if "Live Demo" in project["links"]:
        buttons_html += f'<a href="{project["links"]["Live Demo"]}" class="btn-link btn-primary" target="_blank">🚀 Demo</a>'
    if "GitHub" in project["links"]:
        buttons_html += f'<a href="{project["links"]["GitHub"]}" class="btn-link btn-secondary" target="_blank">💻 Code</a>'

    st.markdown(f"""
    <div class="project-card">
        <div class="card-img-box"><img src="{project['image']}"></div>
        <div class="card-body">
            <div class="card-title">{project['title']}</div>
            <div class="card-desc">{project['description']}</div>
            <div class="badge-container">{badges_html}</div>
            <div class="card-footer">{buttons_html}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_notebook_grid():
    st.write("")
    st.divider()
    st.subheader("🧪 Experiments & Notebooks")
    cols = st.columns(4)
    for i, nb in enumerate(NOTEBOOKS):
        with cols[i % 4]:
            with st.container(border=True):
                st.image(nb['img'], use_container_width=True)
                st.markdown(f"**{nb['name']}**")
                st.markdown(f'<div class="nb-tech-green">🔧 {nb["tech"]}</div>', unsafe_allow_html=True)
                if st.button("Insight 📄", key=f"btn_{i}", use_container_width=True):
                    show_notebook_popup(nb)

# --- 7. MAIN LOGIC ---
def render_projects():
    load_project_css()
    
    # CALLING THE DEV INDICATOR HERE
    render_dev_indicator()
    
    c_text, c_filter = st.columns([3, 1], gap="large")
    with c_text:
        st.markdown("## 🛠️ Project Gallery")
    with c_filter:
        all_tags = sorted(list(set([tag for p in PROJECTS for tag in p["tags"]])))
        selected_tags = st.multiselect("Search", all_tags, label_visibility="collapsed", placeholder="🔍 Filter...")

    st.divider()
    
    filtered_projects = [p for p in PROJECTS if any(tag in selected_tags for tag in p["tags"])] if selected_tags else PROJECTS
    
    if not filtered_projects:
        st.info("No projects found.")
    else:
        cols = st.columns(2, gap="medium")
        for i, project in enumerate(filtered_projects):
            with cols[i % 2]:
                render_project_card(project)
    
    render_notebook_grid()

if __name__ == "__main__":
    render_projects()