import streamlit as st
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFacePipeline, HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

def load_model(model_type, model_name):
    if model_type == "Open-Source":
        if model_name == "HuggingFace - API":
            llm = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation")
            return ChatHuggingFace(llm=llm)
        elif model_name == "HuggingFace - Local":
            llm = HuggingFacePipeline.from_model_id(
                model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                task='text-generation',
                pipeline_kwargs=dict(temperature=0.5, max_new_tokens=100)
            )
            return ChatHuggingFace(llm=llm)

    elif model_type == "Closed-Source (Groq)":
        if model_name == "Groq-LLaMA2":
            return ChatGroq(model_name="llama3-8b-8192")
        elif model_name == "Groq-Mistral":
            return ChatGroq(model_name="gemma2-9b-it")
    return None

def create_prompt(chat_history, user_input):
    prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are a helpful AI assistant. Answer the questions clearly and concisely.'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human', '{question}')
    ])
    return prompt.invoke({"chat_history": chat_history, "question": user_input})

load_dotenv()

# Ensure chat history is initialized
if "chat_history_local" not in st.session_state:
    st.session_state.chat_history_local = []

st.header('LangChain Q&A Assistant')

# Model type selection
model_type = st.selectbox("Choose Model Type:", ["Closed-Source (Groq)", "Open-Source"])

# Model name selection
if model_type == "Open-Source":
    model_name = st.selectbox("Choose Open-Source Model:", ["HuggingFace - API", "HuggingFace - Local"])
else:
    model_name = st.selectbox("Choose Groq Model:", ["Groq-LLaMA2", "Groq-Mistral"])

# User input
user_input = st.text_input("Ask a question:")

if user_input:
    # Load selected model dynamically
    model = load_model(model_type, model_name)
   
    # Append user input to chat history as HumanMessage
    st.session_state.chat_history_local.append(HumanMessage(user_input))

    # Run model using chat history and get result
    result = model.invoke(st.session_state.chat_history_local)

    # Append AI response to chat history
    st.session_state.chat_history_local.append(AIMessage(result.content))

    # Display the response
    st.markdown(result.content)

    # Optionally, display chat history
    if st.checkbox("Show Chat History"):
        for msg in st.session_state.chat_history_local:
            role = "Human" if isinstance(msg, HumanMessage) else "AI"
            st.markdown(f"**{role}**: {msg.content}")