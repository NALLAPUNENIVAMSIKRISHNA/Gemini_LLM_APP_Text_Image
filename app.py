import google.generativeai as genai
import os
import streamlit as st
from dotenv import load_dotenv
load_dotenv()  # loading all the environment variables


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro model and get response
model = genai.GenerativeModel('gemini-2.0-pro-exp')


def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# initialize streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input = st.text_input("Input : ", key="input")
submit = st.button("Ask the question...")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is ")
    st.write(response)
