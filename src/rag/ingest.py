import os
import toml
import time
import shutil
from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# --- CONFIGURATION ---
DATA_PATH_ASSETS = "assets"
DATA_PATH_KB = "src/rag/knowledge_base"
DB_PATH = "src/rag/vector_store"
SECRETS_PATH = ".streamlit/secrets.toml"

def load_secrets():
    if not os.path.exists(SECRETS_PATH):
        raise FileNotFoundError(f"Secrets file not found at {SECRETS_PATH}")
    with open(SECRETS_PATH, "r") as f:
        secrets = toml.load(f)
    return secrets.get("general", {}).get("GOOGLE_API_KEY") or secrets.get("GOOGLE_API_KEY")

def ingest_data():
    try:
        print("-" * 50)
        print("STARTING INTELLIGENT INGESTION")
        print("-" * 50)

        # 1. Load API Key
        api_key = load_secrets()
        os.environ["GOOGLE_API_KEY"] = api_key

        # 2. Load Documents (PDFs + TXT)
        print("Loading documents...")
        documents = []
        
        # Check Assets
        if os.path.exists(DATA_PATH_ASSETS):
            pdf_loader = DirectoryLoader(DATA_PATH_ASSETS, glob="**/*.pdf", loader_cls=PyPDFLoader)
            documents.extend(pdf_loader.load())
            
        # Check Knowledge Base
        if os.path.exists(DATA_PATH_KB):
            txt_loader = DirectoryLoader(DATA_PATH_KB, glob="**/*.txt", loader_cls=TextLoader)
            documents.extend(txt_loader.load())

        if not documents:
            print("Error: No documents found! Check your 'assets' or 'knowledge_base' folders.")
            return

        print(f"Success: Found {len(documents)} document(s).")

        # 3. Split Text
        print("Splitting text...")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(documents)
        print(f"Success: Created {len(chunks)} chunks.")

        # 4. Initialize Embeddings
        print("Initializing Gemini Embeddings...")
        embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

        # 5. Save to Vector Store (Batch Mode)
        print("Saving to ChromaDB (Batch Mode)...")
        
        batch_size = 10
        total_batches = (len(chunks) // batch_size) + 1
        
        # If DB exists, we append to it (Safe Mode)
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i : i + batch_size]
            current_batch = (i // batch_size) + 1
            
            print(f"Processing Batch {current_batch}/{total_batches}...", end="\r")
            
            Chroma.from_documents(
                documents=batch,
                embedding=embeddings,
                persist_directory=DB_PATH
            )
            # Small pause to be nice to the API
            time.sleep(1.5)

        print("\n" + "-" * 50)
        print("INGESTION COMPLETE. The Brain is Ready.")
        print("-" * 50)

    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    ingest_data()