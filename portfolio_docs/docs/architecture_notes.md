# Architecture Notes - DS Portfolio

## Folder structure (recommended)
```
portfolio/
  src/
    ui/
      streamlit_app.py
    api/
      app.py  # FastAPI for GenAI endpoints
    utils/
      llm_client.py
      data_loader.py
  assets/
    projectA.png
    projectB.png
    projectC.png
  docs/
    streamlit_debug_playbook.md
    project_overview.md
  notebooks/
  requirements.txt
```
## Runtime components
- **Streamlit UI** (frontend) — hosts the portfolio and sliders. Talks to backend for GenAI Q&A.  
- **FastAPI backend** — handles LLM calls, caching, authentication (optional), and production endpoints.  
- **LLM client** — wrapper around Gemini/OpenAI with prompt templates and retry logic.  
- **Deployment** — host Streamlit and FastAPI (Render/Heroku for API, Streamlit Cloud or Render for UI).
