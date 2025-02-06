# chat-bot
This is a simple AI-powered chatbot built using Streamlit and OpenAI's GPT models (gpt-3.5-turbo and gpt-4) and llama3-1B model. The chatbot allows users to interact with the AI and maintains chat history within the session.


Technology Used:
1. streamlit- Streamlit is an open-source Python library that allows you to quickly build interactive web applications for machine learning, data visualization, and AI-powered tools using just Python.
2. Python- The core programming language used for developing the application.
3. OpenAI API (openai) - Used to access GPT models (gpt-3.5-turbo & gpt-4) for generating AI responses. Handles user queries and returns AI-generated responses.
4. Hugging Face API- To acccess llama model.
5. Session State (st.session_state)- A feature in Streamlit that maintains chat history across interactions.
   

Features
1. Select between gpt-3.5-turbo, gpt-4 and llama 3.
3. Displays chat history dynamically within the page.
4. Simple UI using Streamlit.
5. Supports real-time interaction.
   

Requirements:
1. Install Dependencies
Make sure you have Python installed, then install the required libraries:
command- pip install streamlit openai
2. OpenAI API Key
To use GPT models, you need an OpenAI API key. Get one from "https://platform.openai.com/api-keys"
3. Hugging-face API Key
To use llama model, you need HF token. Get one from "https://huggingface.co/settings/tokens"

NOTE- Paste both keys in .env file.

Usage
1. Run the Streamlit App
command- streamlit run chat.py

Screenshots:
<img width="957" alt="ss0" src="https://github.com/user-attachments/assets/7fde38d3-28cf-4817-bd3e-d315591a11b4" />
<img width="959" alt="ss1" src="https://github.com/user-attachments/assets/4a21b24a-4aae-4322-a144-31dde5ecce22" />
<img width="959" alt="ss2" src="https://github.com/user-attachments/assets/6526ce8c-c288-417d-9056-bda3bb418228" />
<img width="959" alt="ss3" src="https://github.com/user-attachments/assets/b85523b4-e113-447a-8b2e-fb7f6daffcd7" />

