import os
import streamlit as st
import openai
from dotenv import load_dotenv
from transformers import pipeline
from huggingface_hub import login

#loading environment variables
load_dotenv()

#passing api keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

if not OPENAI_API_KEY or not HF_API_KEY:
    st.error("API keys are missing. Please check your .env file or environment variables.")

#authenticate
login(token=HF_API_KEY)

#main page
st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("AI Chatbot with Multiple LLMs")

#sidebar
if st.sidebar.button("New Chat"):
    st.session_state.messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
    st.rerun()

st.sidebar.header("Models")
model_choice = st.sidebar.selectbox("Select a Model:", ["gpt-3.5-turbo", "gpt-4", "llama-3-1b"])

#calling OpenAI API
def call_openai():
    """Function to call OpenAI GPT models."""
    try:
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model=model_choice, messages=st.session_state.messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

#calling HF LLaMA 3 1B
def call_huggingface_llama():
    """Function to call Hugging Face LLaMA 3 1B model."""
    try:
        generator = pipeline("text-generation", model="meta-llama/Llama-3.2-1B")
        response = generator(st.session_state.messages[-1]['content'], max_length=200)
        return response[0]['generated_text']
    except Exception as e:
        return f"Error: {str(e)}"

#chat History
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful AI assistant."}]

st.write("## Chat History:")
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])

#give input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    if model_choice in ["gpt-3.5-turbo", "gpt-4"]:
        bot_response = call_openai()
    else:
        bot_response = call_huggingface_llama()
    
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.rerun()
