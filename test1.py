import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

# --- CONFIGURATION ---
DB_PATH = "src/rag/vector_store"

def ask_maggie_manual(query):
    # 1. Load API Key
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        return "⚠️ Error: GOOGLE_API_KEY missing in .env file."

    # 2. Connect to Brain (Embeddings)
    # We use the embedding model you confirmed works
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")


    if not os.path.exists(DB_PATH):
        return "⚠️ Error: Database not found. Run ingest.py first!"

    vector_store = Chroma(
        persist_directory=DB_PATH, 
        embedding_function=embeddings
    )
    
    # 3. Retrieve Documents (The "Search" Step)
    print(f"🔎 Searching brain for: '{query}'...")
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})
    docs = retriever.invoke(query)
    
    if not docs:
        return "⚠️ I couldn't find any information on that topic in my database."

    # 4. Build the Context (The "Stuffing" Step)
    # We manually join the text chunks together
    context_text = "\n\n---\n\n".join([d.page_content for d in docs])
    
    # 5. Send to Gemini (The "Chat" Step)
    # We use the Gemini 2.0 Flash model you found
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash", temperature=0.3)
    
    final_prompt = f"""
    You are Maggie, a helpful AI assistant for Prajwal.
    Use the following context to answer the question.
    If the answer is not in the context, say you don't know.
    
    CONTEXT:
    {context_text}
    
    QUESTION:
    {query}
    
    ANSWER:
    """
    
    response = llm.invoke(final_prompt)
    return response.content

if __name__ == "__main__":
    print("🤖 Testing Manual Engine...")
    answer = ask_maggie_manual("What is Prajwal's experience with GenAI?")
    print("\n" + "="*50)
    print(f"📝 ANSWER:\n{answer}")
    print("="*50)
