import streamlit as st
import os
from dotenv import load_dotenv
from app.parser import extract_text_from_pdf
from app.analyzer import analyze_resume

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

# Page config
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #0f1117;}
    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #6C63FF, #FF6584);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle {
        text-align: center;
        color: #888;
        font-size: 1.1rem;
        margin-bottom: 2rem;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #6C63FF, #FF6584);
        color: white;
        border: none;
        padding: 0.75rem;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 600;
        cursor: pointer;
    }
    .stButton > button:hover {
        opacity: 0.9;
    }
    .result-box {
        background-color: #1e1e2e;
        padding: 2rem;
        border-radius: 15px;
        border-left: 4px solid #6C63FF;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<p class="title">📄 AI Resume Analyzer</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your resume and get instant AI-powered feedback!</p>', unsafe_allow_html=True)

st.divider()

# Upload section
col1, col2, col3 = st.columns([1,2,1])
with col2:
    uploaded_file = st.file_uploader("📎 Upload Resume (PDF)", type="pdf")

st.divider()

# Analyze button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    analyze_btn = st.button("🚀 Analyze My Resume")

# Results
if analyze_btn:
    if not uploaded_file:
        st.error("⚠️ Please upload a resume PDF first!")
    else:
        with st.spinner("🤖 AI is analyzing your resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            feedback = analyze_resume(resume_text, api_key)

        st.success("✅ Analysis Complete!")
        st.divider()

        st.markdown('<div class="result-box">', unsafe_allow_html=True)
        st.markdown(feedback)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.divider()
st.markdown('<p style="text-align:center; color:#888;">Built by Tharunika 🚀 | Powered by Groq AI</p>', unsafe_allow_html=True)