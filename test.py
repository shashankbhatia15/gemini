

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
# chat = model.start_chat(history=[])
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
    st.session_state["messages"] = [{"role": "user", "parts": '''you are an AI assistant who follows the following rules for all your answers - 
    1. use space between all words that you give as an output
    2. pformat all the codes in a proper manner
    respond "how may I assist you" if you understand.'''}]
    
    response = model.generate_content(st.session_state.to_dict()['messages'])
    msg = response
    st.session_state.messages.append({"role": "model", "parts": msg.text})
    st.chat_message("assistant").write(msg.text)
    
    # st.session_state.messages.append({"role": "model", "parts": "How can I help you?"})

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["parts"])

if prompt := st.chat_input():


    st.session_state.messages.append({"role": "user", "parts": prompt})
    st.chat_message("user").write(prompt)
    # st.write(st.session_state.to_dict()['messages'])

    # response = model.generate_content(prompt)
    response = model.generate_content(st.session_state.to_dict()['messages'])
    
    msg = response
    st.session_state.messages.append({"role": "model", "parts": msg.text})
    st.chat_message("assistant").write(msg.text)


# z=st.session_state.to_dict()["messages"]
# st.write(type(st.session_state.to_dict()['messages'][2]))
# st.write(st.session_state.to_dict()['messages'])
