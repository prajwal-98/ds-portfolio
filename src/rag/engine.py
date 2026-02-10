import os
import toml
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Load secrets directly to avoid environment issues
SECRETS_PATH = ".streamlit/secrets.toml"

def load_api_key():
    if os.path.exists(SECRETS_PATH):
        with open(SECRETS_PATH, "r") as f:
            secrets = toml.load(f)
        return secrets.get("general", {}).get("GOOGLE_API_KEY") or secrets.get("GOOGLE_API_KEY")
    return os.getenv("GOOGLE_API_KEY")

class RAGEngine:
    def __init__(self):
        self.db_path = os.path.join("src", "rag", "vector_store")
        self.embedding_model = "models/gemini-embedding-001"
        self.llm_model = "models/gemini-flash-latest"
        
        # Ensure API Key is loaded
        os.environ["GOOGLE_API_KEY"] = load_api_key()
        
        self.embeddings = GoogleGenerativeAIEmbeddings(model=self.embedding_model)
        
        # Connect to the Vector Store
        if not os.path.exists(self.db_path):
            raise FileNotFoundError(f"Vector store not found at {self.db_path}. Run ingest.py first.")

        self.vector_db = Chroma(
            persist_directory=self.db_path,
            embedding_function=self.embeddings
        )
        
        # The Persona Prompt
        template = """
        You are an AI Assistant for Prajwal (Maggie).
        Use the following context to answer the question professionally.
        If the answer is not in the context, say you do not know.
        
        Context: {context}
        Question: {question}
        
        Answer:"""
        
        self.prompt = PromptTemplate(
            template=template, 
            input_variables=["context", "question"]
        )

    def get_response(self, user_query):
        llm = ChatGoogleGenerativeAI(model=self.llm_model, temperature=0.3)
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever(search_kwargs={"k": 3}),
            chain_type_kwargs={"prompt": self.prompt}
        )
        
        result = qa_chain.invoke({"query": user_query})
        return result["result"]