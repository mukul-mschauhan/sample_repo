# py --version | Create a virtual env: py -m venv .venv
# Activating the Venv - .venv\Scripts\activate 
# After activating the Virtual Env...install the libraries:
# pip3 install google-generativeai langchain streamlit langchain-google-genai pillow
import streamlit as st

st.title("Movie Recommender System Using Gen AI")
user_input = st.text_input("Enter the Movie Name, Genre (e.g. Comedy or SciFi Movies):") # Act as a Prompt.

# Now we will build the Prompt Template using Langchain.
from langchain_core.prompts import PromptTemplate

template = PromptTemplate(input_variables = ['user_input'],
                          template = "Based on the Preferences, the Movie recommendation for {user_input} is: ")

# Initiate the Google Gemini Model.
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model = "gemini-pro", 
                             google_api_key = "AIzaSyBxBQ_GoFt7dbY1uReLso-8U9mDctobOwo")

# Generate the Recommendation
if user_input:
  prompt = template.format(user_input = user_input)
  response = llm.predict(prompt)
  st.write("Movie Recommendations for you: ", {response})
else:
  st.write("Please enter a movie name or genre.")
  
# Run the following command in terminal - streamlit run main.py