DS Portfolio: FINAL UI MASTER CONTEXT

(Copy this entire block to Gemini 3 or any assistant to sync project state.)

Project identity — short

Project: Prajwal’s Data Science Portfolio (Maggie)
Goal: A modular, recruiter-friendly, premium portfolio showcasing DS + GenAI architecture skills. Three main projects (ML, LLM/GenAI pipeline, Analytics dashboard) will be included later — UI is primary focus first. Built with Streamlit + Python 3.10, Native CSS. No wild hacks.

⸻

High-level site structure (locked)

Navbar (links): Home | About | Career Snapshot | Projects | Resume
Note: Photography is NOT in navbar.

Page order / Pages (locked):
	•	Home (Hero → AI Assistant → Career Snapshot preview/link → Projects preview/link → Footer)
	•	About (full page with interactive cards)
	•	Career Snapshot (full timeline page)
	•	Projects (full projects showcase)
	•	Photography (separate page — accessible via About + Footer only)
	•	Resume (separate page — content later)
	•	Footer (global contact links + photography link)

⸻

Navbar behavior (locked)
	•	Desktop: Toggle button fixed top-right (always visible) → Slide-down slim navbar when clicked. Hidden by default to maximize page space. Auto-collapse after 4s idle or on scroll down. Slide animation: 0.22s easing cubic-bezier(0.4,0,0.2,1).
	•	Mobile: Toggle button top-right → Full-screen overlay menu (stacked large items). Overlay closes on link click, outside tap, or swipe-down.
	•	Toggle is persistent (fixed position) across all pages and screen sizes.

⸻

Home Page (locked)

Order and purpose:
	1.	Hero — centered modern hero, large headline, subtitle changed to:
Data Science | Machine Learning | Generative AI | Databricks | Python
Remove primary CTA; keep secondary CTA only. Remove resume download CTA.
	2.	AI Assistant Showcase — central, shows the LLM assistant feature (chat prompt chips). Floating chat icon present site-wide.
	3.	Career Snapshot (preview) — link to full timeline page.
	4.	Projects (preview) — highlights + link to Projects page.
	5.	Footer.

Hero tagline (locked):
Building scalable Data science and Generative AI solutions from idea → architecture → deployment

⸻

About Page (locked — Two-column + interactive cards)

Layout: Two-column professional layout (Left: Who I Am + What I Do; Right: Skills/Tools grid).

Top section content:
	•	Clean senior-level intro (Who I am, what I do, why DS/GenAI, future goals). Tone: professional, senior architect.

Interactive 3D Card Panel (below About text) — 3 cards (desktop horizontal / mobile stacked):
	1.	Skills Dashboard (card) → click → opens modal popup showing icon grid of core skills/tools (icons only; optional tooltips: years/usage). Icons include: Python, Databricks, Streamlit, PyTorch/Scikit-Learn, Pandas, SQL, Docker, Git, LLM APIs (Gemini/OpenAI), Plotly, MLOps/CICD, Cloud (GCP/AWS).
	2.	Photography / Personal Blog (card) → click → modal preview with short intro + button View Full Photography Gallery → (leads to photography page). Do not load full gallery inside modal.
	3.	Milestones (card) → click → modal listing career & personal milestones (concise bullets: internships, projects, promotions, certifications, notable product impact).

Cards: 3D hover tilt (subtle), on click open modal. On mobile no tilt; tap opens bottom-sheet modal.

⸻

Projects Page (locked)
	•	Hybrid layout: 2 main featured projects + horizontal-scroll gallery of smaller projects.
	•	Cards: image thumbnail; hover shows details overlay; one button: View Live Demo.
	•	Hover effect: blur overlay + 3D lift shadow + arrow slider.
	•	Filters option planned but not required; keep initial implementation without filter, can add later.
	•	Mobile: horizontal swipe carousel for small projects; tap to reveal overlay; “View Live Demo” full width button.

⸻

Career Snapshot Page (locked)
	•	Full-page interactive timeline (desktop horizontal, mobile vertical).
	•	Clicking any node shows detailed card below/aside and timeline slider syncs (click timeline ↔ show details).
	•	No separate filter; timeline nodes should drive content in the detail panel.
	•	Mobile: vertical stacked cards with tap-to-expand.

⸻

Photography Page (placement locked)
	•	Not in navbar, accessible from About page and Footer only.
	•	Page: featured hero/banner, short personal paragraph about photography, 1–2 photography-related mini-project cards (placeholders), masonry gallery (15+ photos), scrollable, click opens lightbox with swipe/pinch on mobile.
	•	On Home page: NO photography preview (we removed it); photography preview was removed to avoid confusion.

⸻

Footer (locked)
	•	Dark background (#1F1F1F or #222).
	•	Left (text): © 2024 – 2025 Prajwal Acharya and Built with Python & Streamlit.
	•	Right (icons): LinkedIn, GitHub, Email (only). Photography link included (small).
	•	No extra design credits. Static footer (appears at bottom only, not sticky).
	•	Icons white, subtle hover.

⸻

Theme & Colors (locked)

Light + Dark themes implemented now (toggle top-right). CSS variable system to switch.

Light theme (default):
	•	--bg: #FFFFFF
	•	--surface: #F9FAFB
	•	--text: #0F1724
	•	--muted: #55606A
	•	--accent: #0EA5A5 (teal)
	•	--accent-contrast: #FFFFFF
	•	--card-shadow: rgba(7,12,21,0.08)
	•	--line: #E6EEF0

Dark theme (.theme-dark overrides):
	•	--bg: #0B0F12
	•	--surface: #0F1720
	•	--text: #E6EEF0
	•	--muted: #9AA6AD
	•	--accent: #2DD4BF
	•	--accent-contrast: #062426
	•	--card-shadow: rgba(2,6,12,0.6)
	•	--line: rgba(255,255,255,0.06)

Note: Accent is teal (not pastel), masculine and modern.

Toggle location: Top-right next to menu toggle; respect prefers-color-scheme default; persist choice in localStorage.

⸻

Typography (locked)

Font family: Inter, sans-serif (single system across site)

Sizing (locked):
	•	H1 (hero): 48–52px desktop / 34–36px mobile; weight 700; line-height 1.15
	•	H2 (section): 32–36px desktop / 22–24px mobile; weight 600
	•	H3: 20–22px desktop / 18px mobile; weight 600
	•	Body: 16–18px desktop / 16px mobile; weight 400; line-height 1.6
	•	Small text/labels: 13–14px; weight 500

Buttons: weight 500, size 15–16px, radius 6–8px.

⸻

Spacing & Layout rules (locked)
	•	Max page width: 1200px center column.
	•	Section vertical spacing: default 96px top & bottom (range 80–100px).
	•	Card padding: 24px desktop / 16px mobile.
	•	Grid gaps: columns 32px; cards 24px; grid elements 20px.
	•	Hero height: ~70–75% screen height (desktop).
	•	Modal padding: 40px desktop / 20px mobile.
	•	Timeline spacing: desktop node gap 320px; mobile node gap 160px.
	•	Gallery gaps: 12px.

⸻

Micro-interactions & Animations (locked)
	•	Navbar slide (desktop): 0.22s, easing cubic-bezier(0.4,0,0.2,1). Auto-collapse after 4s or on scroll down.
	•	Mobile overlay: 0.25s, menu items slide up 20px.
	•	Card hover lift: translateY(-4px), scale 1.01, duration 0.18s, tiny tilt 1°.
	•	Popup modal: scale 0.96 → 1.0 + fade, duration 0.18s.
	•	Buttons hover: +6% brightness, shadow, scale 1.02; active scale down small.
	•	Timeline node & card fade: 0.22s.
	•	Gallery fade-in staggered: 0.15–0.2s per image.
	•	Theme toggle: quick fades 100–150ms, no flash.
	•	Page transitions: cross-fade + slight slide (translateY 8px → 0), duration 240ms. Mobile uses minimal fade 120ms.
	•	Respect prefers-reduced-motion.

⸻

Accessibility / Touch rules (locked)
	•	All touch targets ≥ 44×44 px.
	•	High contrast color checks for buttons & text (WCAG AA).
	•	ARIA labels on interactive elements (hamburger, close, modal, timeline nodes).
	•	Respect reduced motion preference.
	•	Keyboard navigation support for modals.

⸻

Mobile Responsiveness (locked breakpoints & behavior)
	•	Breakpoints: Mobile ≤ 767px; Tablet 768–1023px; Desktop ≥ 1024px.
	•	Mobile decisions:
	•	Stack content vertically.
	•	Projects small cards use horizontal swipe carousel.
	•	About cards stack and open sheet-style modal (max 90% height).
	•	Timeline becomes vertical stacked cards with tap-to-expand.
	•	Photography gallery collapses to 1-column or 2-column based on width, viewer supports swipe/pinch.
	•	Navbar overlay is full screen with large items.
	•	Floating chat icon bottom-right (≥56×56px).
	•	Lazy load images; use responsive srcset.

⸻

Page Transitions (locked)
	•	Primary: cross-fade + slide up (240ms).
	•	Quick anchor/nav jumps: instant jump + 120ms fade.
	•	Modal: scale+fade 180ms.
	•	Mobile: minimal fade 120ms.

⸻

Versioning & snapshot process (locked / recommended)
	•	Use UI_SPEC.md as canonical UI master doc in repo root.
	•	Use CHANGELOG.md (semantic style).
	•	versions/ folder holds snapshots vX.Y.Z/ui_snapshot.md + metadata.json + optional screenshots.
	•	Semantic versioning: MAJOR.MINOR.PATCH rules for UI changes.
	•	Recommended semi-automated workflow: small local script to create versions/vX.Y.Z/, write metadata, append changelog, commit & tag.

⸻

Coding / Cursor rules (how coding chat must behave)
	•	Streamlit + Python 3.10 + Native CSS only.
	•	CRITICAL: The user has unlimited Gemini 2.5 Pro key; when code is requested, NEVER use placeholders. Provide full, copy-pasteable file contents (complete files, with imports). No # rest of code here or ellipses.
	•	Optimize for Cursor Free plan:
	•	Avoid multi-file Composer edits unless user allows.
	•	Produce single-file outputs so user can paste.
	•	Keep explanations minimal and technical.
	•	Respect all project chats and project memory (this chat + others). Do not contradict prior decisions.
	•	Provide recommended Git commit message and tag after generating file outputs.

⸻

Implementation order recommended (locked coding plan — use in coding chat)
	1.	Project skeleton & global CSS/JS/theme variables
	2.	Navbar toggle & theme toggle components
	3.	Global layout, footer, typographic system
	4.	Hero + AI Assistant (UI-only shell)
	5.	About page + 3 interactive cards (modal scaffolding)
	6.	Projects page skeleton + project card component
	7.	Career Snapshot timeline (desktop horizontal + mobile fallback)
	8.	Photography page skeleton + gallery viewer
	9.	Resume page placeholder
	10.	Responsive tuning, accessibility checks, performance optimization
	11.	Create UI snapshot v0.1.0 and commit/tag

⸻

Final operational rules
	•	This UI Master Chat = canonical design record. Use it for any UI decision. Do not code in this chat.
	•	Open a new coding chat (paste the provided coding system prompt) and instruct it: “Implement page X fully — provide full file contents.” The coding chat MUST follow this UI Master Context EXACTLY.
	•	The coding chat must have access to all project chats / memory (i.e., implement everything consistently).