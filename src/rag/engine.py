import os
import toml
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain_core.prompts import PromptTemplate

# --- CONFIGURATION ---
DB_PATH = "src/rag/vector_store"
SECRETS_PATH = ".streamlit/secrets.toml"

def load_secrets():
    if not os.path.exists(SECRETS_PATH):
        return None
    with open(SECRETS_PATH, "r") as f:
        secrets = toml.load(f)
    if "general" in secrets and "GOOGLE_API_KEY" in secrets["general"]:
        return secrets["general"]["GOOGLE_API_KEY"]
    elif "GOOGLE_API_KEY" in secrets:
        return secrets["GOOGLE_API_KEY"]
    return None

def ask_maggie(query):
    try:
        # 1. Setup API Key
        api_key = load_secrets()
        if not api_key:
            return "⚠️ Error: API Key missing."
        os.environ["GOOGLE_API_KEY"] = api_key

        # 2. Initialize Models (Both Google)
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.3)
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        # 3. Load Database
        if not os.path.exists(DB_PATH):
            return "⚠️ Error: Brain not found. Run ingest.py!"
            
        vector_store = Chroma(
            persist_directory=DB_PATH, 
            embedding_function=embeddings
        )

        retriever = vector_store.as_retriever(search_kwargs={"k": 3})

        template = """
        You are Maggie, an AI assistant for Prajwal.
        Context: {context}
        Question: {question}
        Answer:
        """
        prompt = PromptTemplate(template=template, input_variables=["context", "question"])

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever,
            chain_type_kwargs={"prompt": prompt}
        )

        response = qa_chain.invoke(query)
        return response['result']

    except Exception as e:
        return f"❌ Error: {str(e)}"

if __name__ == "__main__":
    print("🤖 Testing Maggie Engine...")
    print(ask_maggie("What is Prajwal's experience with GenAI?"))
