# Issues & Solutions - DS Portfolio

A running list of bugs, errors, and their fixes. Keep short, link to relevant commits or code lines when possible.

---
## 2025-11-25 - Debugger attach crashes (TypeError: 'Task' object is not callable)
**Symptom:** PyCharm debug injection caused Streamlit asyncio loop to throw TypeError and the process died.  
**Fix:** Use Attach-to-Process (attach to worker PID) workflow. Avoid leaving pydevd.settrace or time.sleep in code. Add `.venv` and project folder to AV exclusions if needed.

## 2025-11-24 - Images not found in Streamlit (paths using /mnt/data)
**Symptom:** Images referenced with `/mnt/data/...` inside ChatGPT session don't exist locally.  
**Fix:** Download images and place in `assets/` inside project. Use `st.image("assets/...")` as local reference.

## 2025-11-23 - Git push / branch confusion
**Symptom:** remote origin existed or branch main missing.  
**Fix:** Create branch, set remote correctly, `git push -u origin main` after committing, or create `main` locally: `git checkout -b main` then push.
