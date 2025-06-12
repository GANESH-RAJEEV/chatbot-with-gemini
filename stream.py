
#import the necessary librabries shown
import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

#this function initializes when the user asks the following prompt
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

#this helps in removing the streamlit burger
st.markdown("""                                 
        <style> 
            .st-emotion-cache-vkwuri.eacrzsi18
            {
            visibility:hidden;
            }    
        </style>""",unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'> 🔥ask anything🔥</h1>", unsafe_allow_html=True)   
a=st.chat_input("enter prompt")
# this if statement triggers when the user enters the prompt
if a:            
    press(a)




