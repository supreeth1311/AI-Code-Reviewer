import streamlit as st
import google.generativeai as genai
import os

# Get API key from environment variable (GitHub Secret)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    st.error("API Key Missing! Set GOOGLE_API_KEY in GitHub Secrets.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# System prompts
sys_prompt_ds = """You are a helpful AI Tutor for Data Science.
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible with examples.
If the question is outside data science, politely decline."""

sys_prompt_code = """You are a professional AI Code Reviewer.
Users will submit Python code, and you should:
1. Analyze it for potential bugs, errors, and inefficiencies.
2. Provide a fixed version of the code.
3. Explain necessary improvements.
4. Do not assist with non-Python code.
"""

# Load AI models
model_ds = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",
                                 system_instruction=sys_prompt_ds)
model_code = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",
                                   system_instruction=sys_prompt_code)

# Streamlit UI
st.title("AI Data Science/Code Assistant")

option = st.selectbox("Choose your assistant:", ["Data Science Tutor", "Code Reviewer"])
user_prompt = st.text_area("Enter your query or Python code:", height=200)

btn_click = st.button("Generate Answer")

if btn_click:
    if option == "Data Science Tutor":
        response = model_ds.generate_content(user_prompt)
    else:
        response = model_code.generate_content(user_prompt)
    st.write(response.text)
