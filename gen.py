import os
from dotenv import load_dotenv
import google.generativeai as genai

    # Load environment variables from .env file
load_dotenv()

    # Get the API key
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")


    # Configure the Gemini API
genai.configure(api_key=GEMINI_API_KEY)

    # Example usage (replace with your actual code)
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("write a python code to understand polymorphism only the code no need for explanation" )
print(response.text)
    