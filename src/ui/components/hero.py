# SRC/UI/components/hero.py
from streamlit.components.v1 import html
import streamlit as st

def _build_cards_html(projects):
    cards = []
    for p in projects:
        title = p.get("title", "Untitled")
        subtitle = p.get("subtitle", "")
        img = p.get("image", "")
        link = p.get("link", "#")
        card = f"""
        <div class="card">
          <a href="{link}" target="_blank" class="card-link">
            <div class="card-img" style="background-image: url('{img}');"></div>
            <div class="card-body">
              <h2>{title}</h2>
              <p>{subtitle}</p>
            </div>
          </a>
        </div>
        """
        cards.append(card)
    return "\n".join(cards)

def hero_slider(projects, height=360):
    """
    Render a responsive hero slider using a small HTML/CSS/JS block via streamlit.components.html.
    projects: list of dicts -> {"title": str, "subtitle": str, "image": str, "link": str}
    height: int -> iframe render height (adjust if cards are taller)
    """
    if not projects:
        st.warning("No projects to show in hero slider.")
        return

    cards_html = _build_cards_html(projects)
    html_code = f"""
    <style>
    .hero-wrap {{
      width:100%;
      max-width:1200px;
      margin: 0 auto;
      position: relative;
      overflow: hidden;
      box-sizing: border-box;
      padding: 8px 12px;
    }}
    .slider {{
      display:flex;
      transition: transform 0.45s ease;
      will-change: transform;
    }}
    .card {{
      min-width: 320px;
      max-width: 520px;
      margin-right: 18px;
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 6px 18px rgba(0,0,0,0.08);
      overflow: hidden;
      display:flex;
      flex-direction: column;
    }}
    .card-link {{ color: inherit; text-decoration: none; display:block; height:100%; }}
    .card-img {{
      height: 220px;
      background-size: cover;
      background-position: center;
      width:100%;
    }}
    .card-body {{ padding: 14px; }}
    .card-body h2 {{ margin: 0 0 8px 0; font-size: 20px; line-height:1.1; }}
    .card-body p {{ margin:0; color: #555; font-size: 14px; }}
    .nav-btn {{
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      background: rgba(0,0,0,0.55);
      color: #fff;
      border-radius: 999px;
      width:36px;
      height:36px;
      display:flex;
      align-items:center;
      justify-content:center;
      cursor: pointer;
      z-index: 10;
    }}
    .nav-prev {{ left: 8px; }}
    .nav-next {{ right: 8px; }}
    @media (max-width: 900px) {{
      .hero-wrap {{ padding: 6px; }}
      .card {{ min-width: 280px; margin-right:12px; }}
      .card-img {{ height:180px; }}
    }}
    </style>

    <div class="hero-wrap">
      <div id="slider" class="slider">
        {cards_html}
      </div>
      <div class="nav-btn nav-prev" onclick="prev()">‹</div>
      <div class="nav-btn nav-next" onclick="next()">›</div>
    </div>

    <script>
    const slider = document.getElementById('slider');
    const card = slider.querySelector('.card');
    let index = 0;

    function update() {{
      const w = card.offsetWidth + parseInt(getComputedStyle(card).marginRight);
      slider.style.transform = `translateX(${{-index * w}}px)`;
    }}

    function next() {{
      const cards = slider.querySelectorAll('.card').length;
      const visible = Math.floor(document.querySelector('.hero-wrap').offsetWidth / (card.offsetWidth + 18));
      index = Math.min(index + 1, Math.max(0, cards - (visible || 1)));
      update();
    }}
    function prev() {{
      index = Math.max(0, index - 1);
      update();
    }}

    window.addEventListener('resize', ()=> {{
      const cards = slider.querySelectorAll('.card').length;
      const visible = Math.floor(document.querySelector('.hero-wrap').offsetWidth / (card.offsetWidth + 18));
      index = Math.min(index, Math.max(0, cards - (visible || 1)));
      update();
    }});

    let startX = null;
    slider.addEventListener('touchstart', e => startX = e.touches[0].clientX);
    slider.addEventListener('touchend', e => {{
      if(startX === null) return;
      const endX = e.changedTouches[0].clientX;
      const diff = startX - endX;
      if(Math.abs(diff) > 40) {{
        if(diff > 0) next(); else prev();
      }}
      startX = null;
    }});

    setTimeout(update, 60);
    </script>
    """

    html(html_code, height=height)