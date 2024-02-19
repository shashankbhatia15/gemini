import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

with st.sidebar:

    # Display the logo
    st.image("logo/logo15.png")

    # Add a header for the model options
    st.header("Model Options")

    # Create a selectbox for the model type
    model_name = st.selectbox("Model Type", ["gemini-pro","gemini-1.0-pro-latest", "gemini-1.0-pro", "gemini-1.0-pro-001"])
#best model
# model_name = 'gemini-1.0-pro-latest'
#quite straightforward - not eq
# model_name = 'gemini-1.0-pro'
#good model
# model_name = 'gemini-1.0-pro-001'
#idiot model
# model_name = 'gemini-pro'
generation_config = {
  "temperature": 0.0,
  "top_p": 1,
  "top_k": 1,

}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_ONLY_HIGH"
  },
]


model = genai.GenerativeModel(model_name=model_name,
                              generation_config=generation_config,
                              safety_settings=safety_settings)







# Display the fixed text


try:
    chat = model.start_chat(history=st.session_state['history'])

except:
    chat = model.start_chat(history=[])

if "messages" not in st.session_state:

    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]



for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = chat.send_message(prompt)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg.text})
    st.chat_message("assistant").write(msg.text)

    st.session_state['history']=chat.history
    # st.write(chat.history)
