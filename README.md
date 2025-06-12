# 🔥 Gemini AI Chatbot with Streamlit 🔥

This is a simple yet powerful AI chatbot interface built with **Google's Gemini 2.0 Flash model** and **Streamlit**. It lets users input prompts and receive real-time AI-generated responses — all through a clean web-based chat UI.

---

## 🚀 Features

- 🤖 **Powered by Gemini 2.0 Flash** (via Google Generative AI API)
- 💬 **Interactive chat interface** with user/assistant message bubbles
- 📦 **.env API key management** with `python-dotenv`
- 🧠 Ready for local or cloud deployment



## 🛠️ Installation

1. **Clone the repo:**
   https://github.com/GANESH-RAJEEV/chatbot-with-gemini.git
   ```bash cd gemini-chatbot```

2. 🐍 Create a Virtual Environment (Optional but Recommended)
   ```bash python -m venv venv```
    source venv/bin/activate  # On Windows: venv\Scripts\activate

3. 📥 Install Dependencies
    ```bash pip install -r requirements.txt```

4. 🔑 Set Up Your API Key
Create a .env file in the root folder:
GEMINI_API_KEY=your_google_genai_key_here
You can get your API key from: https://makersuite.google.com/app

▶️ Run the App
streamlit run app.py
Replace app.py with your filename if it’s different.


## 📸 Preview
![chatbot-ui](https://github.com/user-attachments/assets/02edf021-7279-4776-a3d0-95ac2be2055a)






🧾 Sample Code (included in the project)

```python
import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

def press(a):
    load_dotenv()
    GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')
    with st.chat_message("user"):
        st.markdown(a)
    with st.chat_message("assistant"):
        response = model.generate_content(a)
        st.markdown(response.text)

st.markdown("""
        <style> 
            .st-emotion-cache-vkwuri.eacrzsi18
            {
            visibility:hidden;
            }    
        </style>""", unsafe_allow_html=True)
st.markdown("""
 🔥ask anything🔥
""", unsafe_allow_html=True)
a = st.chat_input("enter prompt")
if a:
    press(a)
```


   


