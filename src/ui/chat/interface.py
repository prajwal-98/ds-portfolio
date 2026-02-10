import streamlit as st
from src.rag.engine import RAGEngine

def render_chat_interface(key="global_chat"):
    st.markdown("---")
    st.subheader("Ask My AI Assistant")
    
    # Initialize the Engine once
    if "rag_engine" not in st.session_state:
        try:
            st.session_state.rag_engine = RAGEngine()
        except Exception as e:
            st.error(f"Error initializing AI Engine: {e}")
            return

    # Initialize Chat History (Global)
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display Chat History
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Handle User Input (Using the unique KEY)
    if prompt := st.chat_input("Ask about my skills, projects, or experience...", key=key):
        # 1. Show User Message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Generate AI Response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = st.session_state.rag_engine.get_response(prompt)
                    st.markdown(response)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    st.error(f"An error occurred: {e}")