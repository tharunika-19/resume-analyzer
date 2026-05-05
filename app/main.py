import streamlit as st
import fitz  # PyMuPDF

st.title("Resume Analyzer")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")

if uploaded_file is not None:
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    text = ""
    for page in doc:
        text += page.get_text()

    st.subheader("Extracted Text:")
    st.write(text[:1000])  # showing first 1000 characters