import os


from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
# Import your question-answering code here


# Used to securely store your API key
# from google.colab import userdata





load_dotenv()

GOOGLE_API_KEY= os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.0-pro-001')
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
st.markdown('<div class="fixed-text">💬 ShankCopilot</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "user", "parts": '''you are an AI assistant. 
    '''}]


    st.session_state.messages.append({"role": "model", "parts": "How can I help you?"})

for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).write(msg["parts"])

if prompt := st.chat_input():


    st.session_state.messages.append({"role": "user", "parts": prompt + ' (give reply in a proper readable format)'})

    # ' - use spaces between words in your reply.'
    st.chat_message("user").write(prompt)
    # st.write(st.session_state.to_dict()['messages'])

    # response = model.generate_content(prompt)
    # st.write(st.session_state.to_dict()['messages'][-1])
    response = model.generate_content(st.session_state.to_dict()['messages'][-5:])

    msg = response
    st.session_state.messages.append({"role": "model", "parts": msg.text})
    st.chat_message("assistant").write(msg.text)


# z=st.session_state.to_dict()["messages"]
# st.write(type(st.session_state.to_dict()['messages']))
# st.write(st.session_state.to_dict()['messages'][-4:])
