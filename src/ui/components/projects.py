import streamlit as st

def render_projects_carousel():
    st.markdown("""
        <style>
        .featured-carousel {
            display: flex;
            overflow-x: auto;
            scroll-snap-type: x mandatory;
            gap: 24px;
            padding-bottom: 20px;
            -webkit-overflow-scrolling: touch;
        }
        .featured-card {
            flex: 0 0 100%;
            scroll-snap-align: center;
            background: var(--surface);
            border: 1px solid var(--line);
            border-radius: 16px;
            overflow: hidden;
            max-width: 600px;
            position: relative;
        }
        @media (min-width: 768px) { .featured-card { flex: 0 0 48%; } }
        
        .card-content { padding: 1.5rem; }
        
        .btn-group { display: flex; gap: 10px; margin-top: 1rem; }
        
        .btn-primary {
            padding: 8px 16px; background: var(--surface); border: 1px solid var(--line);
            border-radius: 6px; color: var(--accent); cursor: pointer; text-decoration: none; font-weight: 600;
        }
        .btn-secondary {
            padding: 8px 16px; background: transparent; border: 1px solid transparent;
            border-radius: 6px; color: var(--text-secondary); cursor: pointer; text-decoration: none; font-weight: 500;
        }
        
        /* SCROLLBAR HIDE */
        .featured-carousel::-webkit-scrollbar { display: none; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div style="margin-bottom: 80px; padding: 0 1rem;">', unsafe_allow_html=True)
    st.markdown("### Featured Work")
    
    # HTML String for Project Cards
    projects_html = """
        <div class="featured-carousel">
            <div class="featured-card">
                <div style="height: 200px; background: #2DD4BF; opacity: 0.1;"></div>
                <div class="card-content">
                    <h4>End-to-End GenAI Pipeline</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem;">RAG-based documentation assistant.</p>
                    <div class="btn-group">
                        <a class="btn-primary">View Live Demo</a>
                        <a class="btn-secondary">GitHub Repo</a>
                    </div>
                </div>
            </div>
            <div class="featured-card">
                <div style="height: 200px; background: #0EA5A5; opacity: 0.1;"></div>
                <div class="card-content">
                    <h4>Sales Forecasting Dashboard</h4>
                    <p style="color: var(--text-secondary); font-size: 0.9rem;">Prophet Time-series analytics.</p>
                    <div class="btn-group">
                        <a class="btn-primary">View Live Demo</a>
                        <a class="btn-secondary">GitHub Repo</a>
                    </div>
                </div>
            </div>
        </div>
    """
    st.markdown(projects_html, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
