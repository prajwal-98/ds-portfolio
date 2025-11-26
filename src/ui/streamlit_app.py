# src/ui/streamlit_app.py
import streamlit as st
from pathlib import Path
import os

# -------------------------
# Config / paths
# -------------------------
st.set_page_config(page_title="Prajwal (Maggie) — Portfolio", layout="wide")

# Local assets folder (put your images here)
ASSETS_DIR = Path("assets")
ASSETS_DIR.mkdir(exist_ok=True)

# Session fallback image (for quick testing inside ChatGPT session)
SESSION_SKETCH = "/mnt/data/IMG_5F84E7C8-B38B-4F59-922A-9BCA75A90F94.jpeg"

# -------------------------
# Styles (horizontal images + layout tweaks)
# -------------------------
st.markdown(
    """
    <style>
    /* container border and max width */
    .page-container {
        max-width: 1100px;
        margin: 0 auto;
        padding: 18px;
        border: 1px solid rgba(0,0,0,0.06);
        border-radius: 8px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.04);
    }

    /* wide cinematic image */
    .horizontal-image {
        width: 100%;
        height: 220px;
        object-fit: cover;
        border-radius: 8px;
        display:block;
        margin-bottom: 10px;
    }

    /* thumbnails row */
    .thumb-row {
        display:flex;
        gap:10px;
        align-items:center;
    }
    .thumb {
        width:140px;
        height:70px;
        object-fit:cover;
        border-radius:6px;
        border:1px solid rgba(0,0,0,0.06);
    }

    /* keep chat area tidy */
    .chat-box {
        border: 1px solid rgba(0,0,0,0.06);
        border-radius: 8px;
        padding: 12px;
        background: #fff;
    }

    /* reduce empty gap on smaller screens */
    @media (max-width: 800px) {
        .horizontal-image { height: 160px; }
        .thumb { width:110px; height:60px; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -------------------------
# Helper functions
# -------------------------
def choose_image(local_path: str, session_path: str = SESSION_SKETCH):
    """
    Return a path or URL to use for an image.
    Prefers local_path if exists, otherwise session_path if exists, otherwise a placeholder URL.
    """
    lp = Path(local_path)
    if lp.exists():
        return str(lp), True
    sp = Path(session_path)
    if sp.exists():
        return str(sp), False
    # placeholder image
    return "https://via.placeholder.com/1200x420.png?text=Project+Screenshot", False


def html_img_tag(src: str, css_class: str = "horizontal-image"):
    """Return an HTML img tag for embedding with CSS class"""
    return f'<img src="{src}" class="{css_class}" />'


# -------------------------
# Project data (edit these)
# -------------------------
# Put your real images in assets/projectA.png etc.
PROJECTS = [
    {
        "title": "Project A — ML Pipeline",
        "desc": "End-to-end ML pipeline: EDA, model training, and a Streamlit demo showcasing predictions and evaluation.",
        "techs": ["Python", "scikit-learn", "Streamlit"],
        "image_local": ASSETS_DIR / "projectA.png",
        "demo": "#",
        "repo": "#",
    },
    {
        "title": "Project B — GenAI Pipeline",
        "desc": "LLM-driven format tagging + interactive Q&A with prompt optimisation and caching.",
        "techs": ["Python", "LLM API", "FastAPI"],
        "image_local": ASSETS_DIR / "projectB.png",
        "demo": "#",
        "repo": "#",
    },
    {
        "title": "Project C — Analytics Dashboard",
        "desc": "Interactive competitor analytics with filters, charts and downloadable reports.",
        "techs": ["Pandas", "Plotly", "Streamlit"],
        "image_local": ASSETS_DIR / "projectC.png",
        "demo": "#",
        "repo": "#",
    },
]


# Pre-resolve images and whether they are local
for p in PROJECTS:
    src, is_local = choose_image(str(p["image_local"]))
    p["image_src"] = src
    p["image_is_local"] = is_local


# -------------------------
# Session state defaults
# -------------------------
if "slider_index" not in st.session_state:
    st.session_state.slider_index = 0

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# -------------------------
# Layout: wrapper container
# -------------------------
st.markdown('<div class="page-container">', unsafe_allow_html=True)

# --- HEADER / ABOUT (full width)
col_l, col_r = st.columns([3, 1])
with col_l:
    st.title("Prajwal (Maggie)")
    st.markdown("**Data Scientist • Bangalore**")
    st.markdown(
        "I build production-quality data science pipelines, GenAI systems, and interactive dashboards. "
        "This portfolio highlights 3 hero projects and a live GenAI chat for quick Q&A."
    )
with col_r:
    # sketch or headshot
    sketch_path, sketch_local = choose_image("assets/sketch.jpeg")
    if sketch_local or Path(sketch_path).exists():
        st.markdown(html_img_tag(sketch_path, css_class="horizontal-image"), unsafe_allow_html=True)
    else:
        st.write("Headshot placeholder")

st.markdown("---")

# -------------------------
# MAIN: left = chat, right = projects slider
# -------------------------
left_col, right_col = st.columns([0.45, 0.55])

# LEFT: GenAI chat placeholder (full height card)
with left_col:
    st.header("Ask me anything")
    st.markdown('<div class="chat-box">', unsafe_allow_html=True)
    st.write("Type a question about me, my projects, or technical choices. This is a placeholder — we'll hook a real GenAI backend later.")
    # Show chat history
    for msg in st.session_state.chat_history:
        role = msg.get("role", "user")
        text = msg.get("text", "")
        if role == "user":
            st.markdown(f"**You:** {text}")
        else:
            st.markdown(f"**Maggie (AI):** {text}")

    user_q = st.text_area("Your question", height=90, key="user_q")
    if st.button("Send"):
        if user_q and user_q.strip():
            st.session_state.chat_history.append({"role": "user", "text": user_q.strip()})
            # placeholder reply
            reply = "Placeholder reply — this will come from the GenAI backend later."
            st.session_state.chat_history.append({"role": "assistant", "text": reply})
            st.session_state.user_q = ""
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("Quick links")
    st.markdown("- Resume: (add URL)")
    st.markdown("- GitHub: (add URL)")
    st.markdown("- LinkedIn: (add URL)")

# RIGHT: Project slider + thumbnails
with right_col:
    st.header("Hero Projects")

    # current project
    idx = st.session_state.slider_index % len(PROJECTS)
    proj = PROJECTS[idx]

    # show main cinematic image (with fallback notice)
    st.markdown(f'<div style="margin-bottom:8px;">{html_img_tag(proj["image_src"], "horizontal-image")}</div>', unsafe_allow_html=True)
    if not proj.get("image_is_local", False):
        st.info("Local project image not found — showing placeholder. Add your screenshot to assets/ to replace it.")

    # title + desc + techs + links
    st.subheader(proj["title"])
    st.write(proj["desc"])
    st.markdown(f"**Tech:** {', '.join(proj['techs'])}")
    st.markdown(f"[Live demo]({proj['demo']}) | [GitHub]({proj['repo']})")

    # slider controls
    col_prev, col_center, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("◀ Prev"):
            st.session_state.slider_index = (st.session_state.slider_index - 1) % len(PROJECTS)
            st.experimental_rerun()
    with col_center:
        st.write(f"Project {idx+1} of {len(PROJECTS)}")
    with col_next:
        if st.button("Next ▶"):
            st.session_state.slider_index = (st.session_state.slider_index + 1) % len(PROJECTS)
            st.experimental_rerun()

    st.markdown("---")
    st.subheader("Other projects / Thumbnails")
    # thumbnails row - clickable
    thumb_cols = st.columns(len(PROJECTS))
    for i, p in enumerate(PROJECTS):
        with thumb_cols[i]:
            # clickable button that jumps to project
            if st.button(p["title"], key=f"thumb_btn_{i}"):
                st.session_state.slider_index = i
                st.experimental_rerun()
            # thumbnail image
            st.markdown(f'<img src="{p["image_src"]}" class="thumb" />', unsafe_allow_html=True)
            if not p.get("image_is_local", False):
                st.caption("Add assets/" + f"project{chr(65+i)}.png")

# FOOTER
st.markdown("---")
st.markdown("© 2025 Prajwal (Maggie) — Data Scientist")
st.markdown("GitHub: (add link) • LinkedIn: (add link) • Email: (add)")

st.markdown("</div>", unsafe_allow_html=True)