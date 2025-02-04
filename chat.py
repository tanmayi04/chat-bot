import streamlit as st
import openai

st.set_page_config(page_title="AI Chatbot", layout="wide")
st.title("AI Chatbot with GPT Models")

#sidebar
st.sidebar.header("Choose Your GPT Model")
model_choice = st.sidebar.selectbox("Select a Model:", ["gpt-3.5-turbo", "gpt-4"])

#API key input
openai_api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

#chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant."}]

#function to call OpenAI GPT API
def chat_with_gpt():
    if not openai_api_key:
        return "Please provide an OpenAI API key."
    try:
        client = openai.OpenAI(api_key=openai_api_key)
        response = client.chat.completions.create(
            model=model_choice,
            messages=st.session_state.messages  # Send full conversation history
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

#display chat history
st.write("### Chat History:")
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.write(message["content"])


user_input = st.chat_input("Type your message here...")

if user_input:
    #adding user msg to sessison state
    st.session_state.messages.append({"role": "user", "content": user_input})

    #bot response
    bot_response = chat_with_gpt()

    #adding bot response to session state
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

    st.rerun()
