import os
import streamlit as st
gemini_key = os.environ.get('GEMINI_KEY')

# Now you can use the gemini_key in your Python project
st.write(gemini_key)
