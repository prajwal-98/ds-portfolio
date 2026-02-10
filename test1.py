import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

# Suppress Warnings
warnings.filterwarnings("ignore")

def test_cloud_engine():
    print("--------------------------------------------------")
    print("🚀 TESTING CLOUD ENGINE (Final Config)")
    print("--------------------------------------------------")

    # 1. Load API Key
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        print("❌ Error: GOOGLE_API_KEY not found in .env")
        return

    # 2. Test Chat (We know this works from your last test!)
    print("\n🧠 Checking Chat Intelligence...")
    try:
        llm = ChatGoogleGenerativeAI(model="models/gemini-flash-latest")
        response = llm.invoke("Hi!")
        print(f"   ✅ Chat Online! Response: {response.content}")
    except Exception as e:
        print(f"   ❌ Chat Failed: {e}")
        return

    # 3. Test Memory (Using the CORRECT model you just found!)
    print("\n📚 Checking Memory Systems...")
    try:
        # 👇 CHANGED: using "models/gemini-embedding-001"
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001") 
        vector = embeddings.embed_query("This is a test memory.")
        print(f"   ✅ Memory Online! Vector generated successfully (Length: {len(vector)})")
    except Exception as e:
        print(f"   ❌ Memory Failed: {e}")
        return

    print("\n--------------------------------------------------")
    print("🎉 SYSTEM READY. PROCEED TO PORTFOLIO.")
    print("--------------------------------------------------")

if __name__ == "__main__":
    test_cloud_engine()
