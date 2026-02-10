import os
import toml
import shutil
import time
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- CONFIGURATION ---
DATA_PATH = "src/rag/knowledge_base"
DB_PATH = "src/rag/vector_store"
SECRETS_PATH = ".streamlit/secrets.toml"

def load_secrets():
    if not os.path.exists(SECRETS_PATH):
        raise FileNotFoundError(f"❌ Secrets file not found at {SECRETS_PATH}.")
    with open(SECRETS_PATH, "r") as f:
        secrets = toml.load(f)
    if "general" in secrets and "GOOGLE_API_KEY" in secrets["general"]:
        return secrets["general"]["GOOGLE_API_KEY"]
    elif "GOOGLE_API_KEY" in secrets:
        return secrets["GOOGLE_API_KEY"]
    else:
        raise ValueError("❌ GOOGLE_API_KEY not found in secrets.toml")

def ingest_data():
    try:
        # 1. Load API Key
        print("🔑 Loading Google Gemini API Key...")
        api_key = load_secrets()
        os.environ["GOOGLE_API_KEY"] = api_key

        # 2. Load Documents
        print(f"📂 Loading data from {DATA_PATH}...")
        loader = DirectoryLoader(DATA_PATH, glob="**/*.txt", loader_cls=TextLoader)
        raw_documents = loader.load()
        
        if not raw_documents:
            print("⚠️  No files found!")
            return

        # 3. Split Text
        print("✂️  Splitting text...")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=50,
            separators=["\n\n", "\n", " ", ""]
        )
        chunks = text_splitter.split_documents(raw_documents)
        print(f"   Created {len(chunks)} text chunks.")

        # 4. Initialize Embeddings (Google)
        print("🧠 Initializing Gemini Embeddings...")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        # 5. Reset Database
        if os.path.exists(DB_PATH):
            print("🗑️  Clearing old database...")
            shutil.rmtree(DB_PATH)

        # 6. SLOW INGESTION LOOP
        print("💾 Saving to ChromaDB (Snail Mode: 1 chunk every 30s)...")
        print("   ☕ This will take about 2-3 minutes. Please wait...")
        
        # Create the DB with the first chunk only
        vector_store = Chroma.from_documents(
            documents=[chunks[0]],
            embedding=embeddings,
            persist_directory=DB_PATH
        )
        time.sleep(30) # Wait 30s

        # Add the rest one by one
        for i in range(1, len(chunks)):
            print(f"   Processing chunk {i+1}/{len(chunks)}...", end="\r")
            vector_store.add_documents([chunks[i]])
            time.sleep(30) # FORCE WAIT 30s to avoid 429 error

        print("\n✅ Success! The Brain is ready.")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")

if __name__ == "__main__":
    ingest_data()
