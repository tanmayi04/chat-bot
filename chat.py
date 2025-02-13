import os
import streamlit as st
import openai
from dotenv import load_dotenv
from transformers import pipeline
from huggingface_hub import login
from PIL import Image

#load environment variables
load_dotenv()

#API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")

if not OPENAI_API_KEY or not HF_API_KEY:
    st.error("API keys are missing. Please check your .env file or environment variables.")

#authenticate Hugging Face
login(token=HF_API_KEY)

#set Streamlit page configuration
st.set_page_config(page_title="AI Chatbot", layout="wide")

#session state for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

#login Page
def login_page():
    st.markdown("""
        <style>
        .login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            width: 100%;
        }
        .stTextInput > div > div > input {
            font-size: 18px !important;
            padding: 12px !important;
            border-radius: 8px !important;
            border: 2px solid #4CAF50 !important;
            text-align: center;
        }
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            transition: 0.3s ease;
            cursor: pointer;
            display: block;
            margin: 0 auto;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>🔐 Login to Multi-Model Chatbot</h2>", unsafe_allow_html=True) #emoji from emojipedia

    col1, col2, col3 = st.columns([1, 2, 1])  # Centering
    with col2:
        st.markdown("<div class='login-container'>", unsafe_allow_html=True)
        username = st.text_input("👤 Username", placeholder="Enter your username")
        password = st.text_input("🔑 Password", type="password", placeholder="Enter your password")
        
        col4, col5, col6 = st.columns([1, 2, 1])  # Centering button
        with col5:
            if st.button("Login"):
                if username == "tanmayi" and password == "admin123":  
                    st.session_state["authenticated"] = True
                    st.session_state["username"] = username  
                    st.rerun()
                else:
                    st.error(" Invalid credentials. Please try again.")
        st.markdown("</div>", unsafe_allow_html=True)

#chatbot Page
def chatbot_page():
    st.title(" AI Chatbot with Multiple LLMs")

    #sidebar
    with st.sidebar:
        #new chat button at the top
        if st.button("New Chat"):
            st.session_state.messages = [{"role": "system", "content": "You are a helpful AI assistant."}]
            st.rerun()
        
        st.header("Select Model")
        model_choice = st.selectbox("Choose an AI Model:", ["gpt-3.5-turbo", "gpt-4", "llama-3-1b"])
        
        st.markdown("---")

        #profile Section at Bottom
        st.markdown("### Profile")
        col1, col2 = st.columns([1, 3])
        with col1:
            profile_image = Image.open("profile_icon.png") 
            st.image(profile_image, width=40)
        with col2:
            st.write(f"**{st.session_state['username']}**") 
        
        st.markdown("---") 

        #logout button at the bottom
        if st.button("🚪 Logout"):
            st.session_state["authenticated"] = False
            st.session_state["username"] = ""
            st.rerun()

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

    #chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a helpful AI assistant."}]

    st.write("## Chat History:")
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.write(message["content"])

    #user input
    user_input = st.chat_input("Type your message here...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        bot_response = call_openai() if model_choice in ["gpt-3.5-turbo", "gpt-4"] else call_huggingface_llama()

        st.session_state.messages.append({"role": "assistant", "content": bot_response})
        st.rerun()

#login or chatbot
if not st.session_state["authenticated"]:
    login_page()
else:
    chatbot_page()
