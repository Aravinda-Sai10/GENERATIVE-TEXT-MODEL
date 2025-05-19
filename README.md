                                     AI Text Generator using FLAN-T5

This is a simple and interactive Streamlit web app that uses Google's FLAN-T5 model to generate answers based on your input questions. Powered by Hugging Face Transformers, this tool can answer questions, explain concepts, and more — all with a beautiful UI.

---

# FEATURES:

- Uses `google/flan-t5-large` via Hugging Face Transformers
- Clean Streamlit interface with custom CSS
- Handles user input interactively
- Caches model to avoid reloading every time
---

# APP PREVIEW:

![APP PREVIEW](screenshots/OUTPUT%201.png)
# WORKING:
![OUTPUT 2](https://github.com/user-attachments/assets/4a26581d-8826-4912-8c17-5898d87c44cd)

---

## 📂 FILE STRUCTURE:

neural-style-transfer-app/
│
├── app.py                  # Main Streamlit app
├── style.css               #  CSS for UI styling
├── requirements.txt        # Python dependencies
├── .gitignore              # Files to ignore in Git
└── screenshots/
    └── output.png  


# TECH STACK:
   - Frontend: Streamlit + Custom CSS

   - Backend: Hugging Face Transformers

   - Model: google/flan-t5-large (via pipeline)


#  HOW TO RUN:

1. Clone this repository:
   
   git clone https://github.com/Aravinda-Sai10/Text-Generator.git
   cd Text-Generator

2. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   streamlit run app.py

---

# HOW IT WORKS:

1. The app loads the **FLAN-T5 model** using `transformers.pipeline("text2text-generation")`.
2. The user enters a question or prompt.
3. When they click "🔍 Get Answer", the app:
   - Sends the question to the model
   - Receives a generated response
   - Displays the answer interactively

---
# USES:
1.**Question Answering**         – Get concise answers to general knowledge or factual queries.
2.**Educational Assistance**     – Ask study-related questions and receive simplified explanations.
3.**Personal Assistant Tasks**   – Quickly get definitions, summaries, or information without Googling.
4.**Prototype AI Chatbot**       – Use it as a base to build more advanced conversational AI apps.
