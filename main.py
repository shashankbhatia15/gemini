

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
st.markdown(
    """
    <style>
    .fixed-text {
        position: fixed;
        top: 60px;
        left: 20px;
        background-color: grey;
        padding: 10px;
        font-size: 24px; /* Adjust the font size as needed */
        font-weight: bold; /* Make the text bold */
        border: 1px solid #ccc;
        border-radius: 50px;
        z-index: 1;
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Display the fixed text
st.markdown('<div class="fixed-text">💬 ShankGPT</div>', unsafe_allow_html=True)

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
