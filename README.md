# chat-bot
This is a simple AI-powered chatbot built using Streamlit, OpenAI's GPT models (gpt-3.5-turbo and gpt-4) and llama3-1B model. The chatbot allows users to interact with the AI and maintains chat history within the session.


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
1. Install Dependencies:
Make sure you have Python installed, then install the required libraries:
command- pip install streamlit openai
2. OpenAI API Key:
To use GPT models, you need an OpenAI API key. Get one from "https://platform.openai.com/api-keys"
3. Hugging-face API Key:
To use llama model, you need HF token. Get one from "https://huggingface.co/settings/tokens"

NOTE- Paste both keys in .env file.

Usage
1. Run the Streamlit App
command- streamlit run chat.py

Screenshots:
![Screenshot 2025-02-13 134656](https://github.com/user-attachments/assets/48499827-e95d-4584-b79e-7bb35eca34cb)

![Screenshot 2025-02-13 134803](https://github.com/user-attachments/assets/c92ae6d0-cf18-4166-a4c7-c006ddc2dbfc)

<img width="959" alt="Screenshot 2025-02-13 134948" src="https://github.com/user-attachments/assets/12f3ab03-f93f-4f62-ba78-bc6d30c0686b" />

<img width="953" alt="Screenshot 2025-02-13 135147" src="https://github.com/user-attachments/assets/2a3bb741-708d-4299-b245-64c45ae50213" />
