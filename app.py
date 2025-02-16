import streamlit as st
import google.generativeai as genai

# Configure API Key (Ensure it's securely stored in a .env file or Streamlit secrets)
genai.configure(api_key="YOUR_API_KEY")

# System Prompts
sys_prompt_ds = """You are a helpful AI Tutor for Data Science.
Students will ask you doubts related to various topics in data science.
You are expected to reply in as much detail as possible.
Make sure to take examples while explaining a concept.
In case a student asks any question outside the data science scope,
politely decline and tell them to ask only data science-related questions."""

sys_prompt_code = """You are a professional AI Code Reviewer.
Users will submit Python code, and you should:
1. Analyze it for potential bugs, errors, and inefficiencies.
2. Provide a fixed version of the code.
3. Explain the necessary changes and improvements.
4. Do not provide assistance for non-Python code."""

# Initialize Models
model_ds = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",
                                 system_instruction=sys_prompt_ds)

model_code = genai.GenerativeModel(model_name="models/gemini-2.0-flash-exp",
                                   system_instruction=sys_prompt_code)

# ------------- Streamlit UI Enhancements -------------
# Sidebar with App Info
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Google_Gemini_logo.svg/1024px-Google_Gemini_logo.svg.png", width=120)
st.sidebar.title("AI Code Reviewer & Data Science Tutor")
st.sidebar.markdown("🚀 Ask questions related to Data Science or get your Python code reviewed!")

# Main Title with Styling
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>AI Data Science & Code Assistant</h1>",
            unsafe_allow_html=True)

# User Selection
option = st.selectbox("🔹 Choose your assistant:", ["Data Science Tutor", "Code Reviewer"])

# User Input Section
user_prompt = st.text_area("💬 Enter your query or Python code:", height=200, placeholder="Type your question or paste your Python code here...")

# Generate Answer Button
if st.button("🚀 Generate Answer"):
    if user_prompt.strip():  # Check if input is not empty
        with st.spinner("Thinking... 🤖"):
            response = model_ds.generate_content(user_prompt) if option == "Data Science Tutor" else model_code.generate_content(user_prompt)

        # Display response
        st.subheader("🔍 AI Response:")
        st.write(response.text)

        # Expandable Section for Detailed Explanation
        with st.expander("📌 See Explanation"):
            st.write("Here’s a breakdown of your query or code:")

        # Provide a downloadable version (if applicable)
        if option == "Code Reviewer":
            st.download_button(label="📥 Download Fixed Code",
                               data=response.text,
                               file_name="fixed_code.py",
                               mime="text/plain")
    else:
        st.warning("⚠️ Please enter a query or code before generating a response.")

