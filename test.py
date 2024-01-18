import os
import streamlit as st
gemini_key = os.environ.get('GEMINI_KEY')

# Now you can use the gemini_key in your Python project
# st.write(gemini_key)
import requests

# Replace these values with your own PAT and secret name
pat = "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"
secret_name = "GEMINI_KEY"

# Make a request to the GitHub Secrets API to retrieve the secret
response = requests.get(
    f"https://api.github.com/repos/YOUR_REPOSITORY/secrets/{secret_name}",
    headers={"Authorization": f"token {pat}"},
)

# Parse the response to extract the secret value
secret_value = response.json()["value"]

# Use the secret value in your code
print(secret_value)
