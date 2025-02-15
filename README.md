import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyD1Gt4fuV23MybKvkU5vi7X1w8F3KRxl_o")

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

model_ds = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",
system_instruction=sys_prompt_ds)

model_code = ai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",
system_instruction=sys_prompt_code)

st.title("AI Data science/Code Assistant ")

option = st.selectbox("Choose your assistant:", ["Data Science Tutor", "Code Reviewer"])

user_prompt = st.text_area("Enter your query or Python code:", height=200)

btn_click = st.button("Generate Answer")

if btn_click:
    if option == "Data Science Tutor":
        response = model_ds.generate_content(user_prompt)
    else:
        response = model_code.generate_content(user_prompt)
    st.write(response.text)
