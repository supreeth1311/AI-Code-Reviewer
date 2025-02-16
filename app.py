import streamlit as st
import google.generativeai as genai

# Configure API Key
genai.configure(api_key="AIzaSyD1Gt4fuV23MybKvkU5vi7X1w8F3KRxl_o")

# System Prompts
sys_prompt_ds = """You are a helpful AI Tutor for Data Science.
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining a concept.
In case a student asks any question outside the data science scope,
politely decline and tell them to ask the question from the data science domain only."""

sys_prompt_code = """You are a professional AI Code Reviewer.
Users will submit Python code, and you should:
1. Analyze it for potential bugs, errors, and inefficiencies.
2. Provide a fixed version of the code.
3. Explain the necessary changes and improvements.
4. Do not provide assistance for non-Python code.
"""

# Initialize models with correct names
model_ds = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=sys_prompt_ds)
model_code = genai.GenerativeModel(model_name="gemini-1.5-flash", system_instruction=sys_prompt_code)

# Streamlit UI
st.title("AI Data Science/Code Assistant")

option = st.selectbox("Choose your assistant:", ["Data Science Tutor", "Code Reviewer"])
user_prompt = st.text_area("Enter your query or Python code:", height=200)

if st.button("Generate Answer"):
    if user_prompt.strip():
        if option == "Data Science Tutor":
            response = model_ds.generate_content(user_prompt)
        else:
            response = model_code.generate_content(user_prompt)
        
        st.write(response.text)
    else:
        st.warning("Please enter a query or Python code.")
