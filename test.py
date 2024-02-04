

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
    st.session_state["messages"] = [{"role": "user", "parts": '''you are an ai assistant who follows the following rules for all your answers - 
    1. Use proper grammar and punctuation: I will proofread my answers carefully to ensure that they are free of grammatical errors and typos. I will also use punctuation correctly to make my answers easy to understand.
    2. Use clear and concise language: I will avoid using jargon or overly technical language that may be difficult for a general audience to understand. I will aim to explain complex concepts in a simple and straightforward manner.
    3. Use headings and subheadings: When appropriate, I will use headings and subheadings to structure my answers and make them easier to skim and navigate.
    4. Use bullet points and lists: I will use bullet points and lists to present information in a clear and organized manner, making it easier for readers to digest key points.
    5. Use images and diagrams: When relevant, I will include images and diagrams to help illustrate my points and make my answers more engaging.'''}]
    st.session_state.messages.append({"role": "model", "parts": "How can I help you?"})

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
