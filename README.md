                                     AI Text Generator using FLAN-T5

This is a simple and interactive Streamlit web app that uses Google's FLAN-T5 model to generate answers based on your input questions. Powered by Hugging Face Transformers, this tool can answer questions, explain concepts, and more — all with a beautiful UI.

---

# FEATURES:

- Uses `google/flan-t5-large` via Hugging Face Transformers
- Clean Streamlit interface with custom CSS
- Handles user input interactively
- Caches model to avoid reloading every time
---

# SCREENSHOTS:

![APP PREVIEW](screenshots/OUTPUT%201.png)

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

1. Create and activate a virtual environment:
   python -m venv venv
   source venv/bin/activate  

2. Install dependencies:
   pip install -r requirements.txt

3. Run the app:
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
