# Import necessary libraries
import streamlit as st  # For creating the web app
from transformers import pipeline  # For using the FLAN-T5 text generation model
import os  # For checking if the CSS file exists

# Setting Streamlit page configuration
st.set_page_config(page_title="AI Text Generator", page_icon="🤖", layout="centered")

# Function to load and apply custom CSS styling
def load_css():
    css_file = "style.css"
    if os.path.exists(css_file):
        with open(css_file) as f:
            css_content = f.read()
            st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ styles.css not found. Custom styles won't apply.")

# Call the function to apply styles
load_css()

# Load the FLAN-T5 model using Hugging Face pipeline
@st.cache_resource  # Cache the model so it's not loaded again on every run
def load_qa_model():
    return pipeline("text2text-generation", model="google/flan-t5-large")

# Store the model in a variable
qa_pipeline = load_qa_model()


# Title of the app
st.markdown("<h1 class='main-title'>Text Generator</h1>", unsafe_allow_html=True)

# Subtitle with custom class
st.markdown("<p class='description'>Ask anything and get real answers instantly using FLAN-T5</p>", unsafe_allow_html=True)
 
 
# Text input box for user to ask a question
user_question = st.text_input("❓ Ask a question")

# When user clicks the "Get Answer" button
if st.button("Get Answer"):
    # Check if the input is not empty
    if user_question.strip() == "":
        # Show a warning if input is empty
        st.warning("Please enter a valid question.")
    else:
        # Show spinner while generating answer
        with st.spinner("Generating answer..."):
            # Generate answer using the model
            result = qa_pipeline(user_question, max_length=256, temperature=0.7, do_sample=True)
            # Extract the answer text
            answer = result[0]["generated_text"]
            # Show the answer to the user
            st.markdown("### 💡 Answer:")
            st.success(answer)
