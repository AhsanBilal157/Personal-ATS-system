import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import os
import PyPDF2

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def extract_text_from_pdf(uploaded_file):
    if uploaded_file is not None:
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ''
        for page_num in range(len(reader.pages) ):
            page = reader.pages[page_num] 
            text += page.extract_text()
        return text
    else:
        raise FileNotFoundError("No file uploaded")

def get_llm_response(input_text, cv_content, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_text, cv_content, prompt])
    generated_text = response.candidates[0].content.parts[0].text
    return generated_text

st.header("ATS System")
txt_input = st.text_area("Job Description: ")
uploaded_file = st.file_uploader("Upload CV", type=['pdf'])

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")
submit2 = st.button("How Can I Improvise my Skills")
submit3 = st.button("What are the Keywords That are Missing")
submit4 = st.button("Percentage match")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager, your task is to review the provided resume against the job description. 
 Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an Technical Human Resource Manager with expertise in data science, 
your role is to scrutinize the resume in light of the job description provided. 
Share your insights on the candidate's suitability for the role from an HR perspective. 
Additionally, offer advice on enhancing the candidate's skills and identify areas where improvement is needed.
"""

input_prompt3 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. As a Human Resource manager,
 assess the compatibility of the resume with the role. Give me what are the keywords that are missing
 Also, provide recommendations for enhancing the candidate's skills and identify which areas require further development.
"""

input_prompt4 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality. 
Your task is to evaluate the resume against the provided job description. Give me the percentage match of the resume to the job description. 
First, provide the percentage in numbers , then list the missing keywords, and finally provide your thoughts.
"""

if submit1:
    if uploaded_file is not None:
        file_content = extract_text_from_pdf(uploaded_file)
        response = get_llm_response(txt_input, file_content, input_prompt1)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit2:
    if uploaded_file is not None:
        file_content = extract_text_from_pdf(uploaded_file)
        response = get_llm_response(txt_input, file_content, input_prompt2)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit3:
    if uploaded_file is not None:
        file_content = extract_text_from_pdf(uploaded_file)
        response = get_llm_response(txt_input, file_content, input_prompt3)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")

if submit4:
    if uploaded_file is not None:
        file_content = extract_text_from_pdf(uploaded_file)
        response = get_llm_response(txt_input, file_content, input_prompt4)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload the resume")
