import streamlit as st
import os
from dotenv import load_dotenv
from app.parser import extract_text_from_pdf
from app.analyzer import analyze_resume

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Page config
st.set_page_config(page_title="Resume Analyzer", page_icon="📄")

# Title
st.title("📄 AI Resume Analyzer")
st.write("Upload your resume and get instant AI-powered feedback!")

# File upload
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type="pdf")

# Analyze button
if st.button("Analyze Resume"):
    if not uploaded_file:
        st.error("Please upload a resume PDF!")
    else:
        with st.spinner("Analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            feedback = analyze_resume(resume_text, api_key)
            st.success("Analysis Complete!")
            st.markdown(feedback)