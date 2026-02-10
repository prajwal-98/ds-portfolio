import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

print("🔍 Scanning for MEMORY (Embedding) models...")
try:
    for m in genai.list_models():
        # This checks for MEMORY capability (embedContent)
        if 'embedContent' in m.supported_generation_methods:
            print(f"   ✅ FOUND: {m.name}")
except Exception as e:
    print(f"❌ Error: {e}")
