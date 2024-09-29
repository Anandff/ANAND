import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyDVl0NJXaVcVsx71vdhlW_78yQ33hlnalg")

model=genai.GeinerativeModel('gemini-1.5-flash0')

def get_gemini_response (input_text, image_data, prompt):
    response = model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details (uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Was Uploaded")
    
st.set_page_config(page_title="anand's invoice generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made by Anand")
st.sidebar.write("powered by google gemini")
st.header("RoboBill")
st.subheader("Made by anand")
st.subheader("manage your expenses with RoboBill")
input = st.text_input("What do you want me to do?",key="input")
uploaded_file=st.file_uploader("choose a image",type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True)

ssubmit=st.button("Let's Go")

input_prompt= """
you are an expert in reading invoices. we are going to upload an image of an in and oyu will have to answer any type of question that the
user asks you. you have to greet the user first. make sure to keep the fonts uniform and give the items list in a point-wise format.
at the end, make sure to repeat the name of out app "RoboBill" and ask the user to use it again.
"""
if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt, image_data, input)
    st.subheader("here's what you need to know")
    st.write(response)
