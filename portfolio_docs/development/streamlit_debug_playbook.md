# Streamlit Debug Playbook — Prajwal (Maggie)

**Where to add:** `docs/streamlit_debug_playbook.md` in repo and also upload to ChatGPT Project under `development/`.

## Purpose
Repeatable steps to debug Streamlit + PyCharm on Windows. Use Attach-to-Process method for stability.

## Daily Workflow (recommended)
1. In project terminal run:
   ```powershell
   .venv\Scripts\python.exe -m streamlit run src/ui/streamlit_app.py --logger.level=debug
   ```
2. In PyCharm: Run → Attach to Process… → pick the worker (higher PID).
3. Put breakpoints in `src/ui/streamlit_app.py` and refresh browser.
4. Debug. Stop server in terminal when done.
