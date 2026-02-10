import streamlit as st
import textwrap # Add this if you want to be safe, or just use the code below

# --- 1. MAIN FEATURED PROJECTS (The "Big 4") ---
PROJECTS = [
    {
        "title": "GenAI Portfolio Website",
        "category": "GenAI",
        "tags": ["Streamlit", "LangChain", "RAG", "ChromaDB"],
        "description": "A personal portfolio engine featuring a self-aware RAG chatbot. It ingests my resume/codebase and answers questions.",
        "links": {"GitHub": "#", "Live Demo": "#"},
        "image": "https://placehold.co/600x400/2E3B55/FFF?text=GenAI+Portfolio"
    },
    {
        "title": "Enterprise LLM Tagging System",
        "category": "GenAI",
        "tags": ["Python", "OpenAI API", "Batch Processing"],
        "description": "Designed a batch-processing system to tag thousands of product descriptions. Reduced API costs by 30%.",
        "links": {"GitHub": "#"},
        "image": "https://placehold.co/600x400/E74C3C/FFF?text=LLM+Tagger"
    },
    {
        "title": "High-Volume Data Pipeline",
        "category": "Data Engineering",
        "tags": ["PySpark", "Databricks", "SQL"],
        "description": "Built an end-to-end pipeline merging complex datasets from multiple zones with automated audit logs.",
        "links": {"GitHub": "#"},
        "image": "https://placehold.co/600x400/27AE60/FFF?text=Data+Pipeline"
    },
    {
        "title": "Visual Data Validator",
        "category": "Data Analysis",
        "tags": ["Pandas", "Streamlit", "Data Visualization"],
        "description": "A utility tool for comparing 'Old vs New' datasets. Visualizes schema changes and row counts.",
        "links": {"GitHub": "#"},
        "image": "https://placehold.co/600x400/F1C40F/333?text=Data+Validator"
    }
]

# --- 3. HELPER: RENDER MAIN CARD ---
def render_project_card(project):
    """Renders a detailed card for featured projects."""
    with st.container(border=True):
        st.image(project["image"], use_container_width=True)
        st.subheader(project["title"])
        st.write(" ".join([f"`{tag}`" for tag in project["tags"]]))
        st.caption(project["description"])
        cols = st.columns(len(project["links"]))
        for i, (label, url) in enumerate(project["links"].items()):
            with cols[i]:
                st.link_button(label, url, use_container_width=True)

# --- 2. UPDATED NOTEBOOK DATA (With Images & Perfect Sizes) ---
# We use relevant placeholder images for a visual "collage" feel
NOTEBOOKS = [
    {
        "name": "Churn Prediction", 
        "tech": "XGBoost", 
        "size": "card-wide", 
        "img": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80"
    },
    {
        "name": "Movie Recommender", 
        "tech": "SVD / Matrix Fac", 
        "size": "card-tall", 
        "img": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=600&q=80"
    },
    {
        "name": "Stock Forecasting", 
        "tech": "LSTM / TensorFlow", 
        "size": "card-big", 
        "img": "https://images.unsplash.com/photo-1611974765270-ca1258634369?w=600&q=80"
    },
    {
        "name": "Titanic EDA", 
        "tech": "Seaborn", 
        "size": "card-medium", 
        "img": "https://images.unsplash.com/photo-1524661135-423995f22d0b?w=600&q=80"
    },
    {
        "name": "Twitter Sentiment", 
        "tech": "NLTK / VADER", 
        "size": "card-medium", 
        "img": "https://images.unsplash.com/photo-1611605698389-377a032434f6?w=600&q=80"
    },
    {
        "name": "Housing Prices", 
        "tech": "Scikit-Learn", 
        "size": "card-wide", 
        "img": "https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600&q=80"
    },
    {
        "name": "Image Classifier", 
        "tech": "PyTorch / CNN", 
        "size": "card-tall", 
        "img": "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=600&q=80"
    },
    {
        "name": "Credit Fraud", 
        "tech": "Anomaly Detect", 
        "size": "card-medium", 
        "img": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&q=80"
    },
    {
        "name": "Farudulant", 
        "tech": "Anomaly Detect", 
        "size": "card-medium", 
        "img": "https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=600&q=80"
    },
    {
        "name": "Spotify Viz", 
        "tech": "Plotly", 
        "size": "card-medium", 
        "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?w=600&q=80"
    },
    {
        "name": "FMCG",
        "tech": "Plotly", 
        "size": "card-medium", 
        "img": "https://images.unsplash.com/photo-1614680376593-902f74cf0d41?w=600&q=80"
    },
    {
        "name": "Resume Parser", 
        "tech": "Spacy / NLP", 
        "size": "card-wide", 
        "img": "https://images.unsplash.com/photo-1586281380349-632531db7ed4?w=600&q=80"
    },
]

# --- 4. HELPER: RENDER NOTEBOOK COLLAGE (Visual Masonry) ---
def render_notebook_collage():
    st.write("")
    st.divider()
    st.subheader("🧪 Experiments & Notebooks")
    st.caption("A visual collection of my EDA and POC work.")

    st.markdown("""
    <style>
        /* THE CONTAINER */
        .collage-grid {
            display: grid;
            /* Force 4 columns on desktop for perfect packing */
            grid-template-columns: repeat(4, 1fr); 
            grid-auto-rows: 150px; /* Fixed row height */
            gap: 12px;
            grid-auto-flow: dense; /* Fills holes automatically */
            padding: 10px 0;
        }

        /* THE CARD */
        .notebook-card {
            position: relative;
            border-radius: 12px;
            overflow: hidden;
            text-decoration: none;
            transition: transform 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        /* BACKGROUND IMAGE LAYER */
        .card-bg {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background-size: cover;
            background-position: center;
            transition: transform 0.5s ease;
            z-index: 1;
        }

        /* OVERLAY FOR TEXT READABILITY */
        .card-overlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(to top, rgba(0,0,0,0.9), rgba(0,0,0,0.2));
            z-index: 2;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 15px;
            opacity: 0.9;
        }

        /* HOVER EFFECTS */
        .notebook-card:hover { transform: scale(1.02); z-index: 10; }
        .notebook-card:hover .card-bg { transform: scale(1.1); }
        .notebook-card:hover .card-overlay { background: linear-gradient(to top, rgba(0,0,0,0.95), rgba(0,0,0,0.4)); }

        /* TEXT STYLES */
        .nb-title { color: white; font-weight: 700; font-size: 14px; margin-bottom: 4px; text-shadow: 0 2px 4px rgba(0,0,0,0.5); }
        .nb-tech { color: #ddd; font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.5px; }

        /* SIZING CLASSES */
        .card-medium { grid-column: span 1; grid-row: span 1; }
        .card-wide   { grid-column: span 2; grid-row: span 1; }
        .card-tall   { grid-column: span 1; grid-row: span 2; }
        .card-big    { grid-column: span 2; grid-row: span 2; }

        /* MOBILE RESPONSIVENESS */
        @media (max-width: 768px) {
            .collage-grid { grid-template-columns: repeat(2, 1fr); }
        }
    </style>
    """, unsafe_allow_html=True)

    # HTML GENERATION
    html_content = '<div class="collage-grid">'
    for nb in NOTEBOOKS:
        size = nb.get('size', 'card-medium')
        link = nb.get('link', '#')
        img_url = nb.get('img', '')
        
        html_content += f"""
        <a href="{link}" class="notebook-card {size}">
            <div class="card-bg" style="background-image: url('{img_url}');"></div>
            <div class="card-overlay">
                <div class="nb-title">{nb['name']}</div>
                <div class="nb-tech">{nb['tech']}</div>
            </div>
        </a>"""
    
    html_content += "</div>"
    st.markdown(html_content, unsafe_allow_html=True)

# --- 5. MAIN PAGE RENDERER ---

def render_projects():
    st.title("🛠️ Project Gallery")
    st.markdown("Here is a selection of my recent work in **Generative AI**, **Data Engineering**, and **Full-Stack Data Science**.")
    
    # --- A. FILTER SECTION ---
    all_tags = sorted(list(set([tag for p in PROJECTS for tag in p["tags"]])))
    selected_tags = st.multiselect("🔍 Filter Featured Projects:", options=all_tags, default=None)
    
    st.write("") # Spacer

    # --- B. FILTER LOGIC ---
    if selected_tags:
        filtered_projects = [p for p in PROJECTS if any(tag in selected_tags for tag in p["tags"])]
    else:
        filtered_projects = PROJECTS

    # --- C. MAIN GRID RENDER ---
    if not filtered_projects:
        st.info("No projects match these filters.")
    else:
        cols = st.columns(2, gap="medium")
        for i, project in enumerate(filtered_projects):
            with cols[i % 2]:
                render_project_card(project)

    # --- D. THE NOTEBOOK COLLAGE (Always visible at bottom) ---
    
    render_notebook_collage()


