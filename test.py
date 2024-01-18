

import pathlib
import textwrap

import google.generativeai as genai
import streamlit as st
# Import your question-answering code here


# Used to securely store your API key
# from google.colab import userdata




# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY='AIzaSyDoBhE1leGM_nBGdJPLgDQx46OyViTn2Q4'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
# chat
# First
import streamlit as st

# st.title("💬 ShankGPT")
header = st.container()
with header:
    st.title("My Streamlit App")
st.experimental_set_query_params(fixed_header=True)

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
