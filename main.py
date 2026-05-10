import streamlit as st
import os
from dotenv import load_dotenv
from app.parser import extract_text_from_pdf
from app.analyzer import analyze_resume

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    * { font-family: 'Inter', sans-serif; }

    .main { background-color: #07070f; }

    [data-testid="stAppViewContainer"] {
        background-color: #07070f;
    }

    [data-testid="stVerticalBlock"] > [data-testid="stVerticalBlock"] {
        background: linear-gradient(145deg, #13131f, #1a1a2e);
        border: 1px solid #2a2a3e;
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 8px 40px rgba(108, 99, 255, 0.12);
    }

    .hero {
        text-align: center;
        padding: 1rem 0 1.5rem 0;
    }
    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, #6C63FF22, #FF658422);
        border: 1px solid #6C63FF55;
        color: #6C63FF;
        padding: 0.35rem 1rem;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-bottom: 1.2rem;
        letter-spacing: 1px;
    }
    .hero-title {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #6C63FF 50%, #FF6584 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 0.8rem;
    }
    .hero-subtitle {
        color: #888;
        font-size: 1rem;
        max-width: 420px;
        margin: 0 auto;
        line-height: 1.6;
    }
    .stats-container {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 0.8rem;
        margin: 1.5rem 0;
    }
    .stat-box {
        background: #0a0a0f;
        border: 1px solid #2a2a3e;
        border-radius: 14px;
        padding: 1rem 0.5rem;
        text-align: center;
    }
    .stat-number {
        font-size: 1.6rem;
        font-weight: 800;
        color: #6C63FF;
    }
    .stat-label {
        font-size: 0.72rem;
        color: #666;
        margin-top: 0.2rem;
    }
    .upload-label {
        color: #ffffff;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .section-divider {
        border: none;
        border-top: 1px solid #2a2a3e;
        margin: 1.2rem 0;
    }
    .result-box {
        background: #0a0a0f;
        border: 1px solid #6C63FF44;
        border-radius: 16px;
        padding: 1.5rem;
        margin-top: 1rem;
        color: #ddd;
        line-height: 1.8;
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #6C63FF, #FF6584) !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem !important;
        border-radius: 12px !important;
        font-size: 1rem !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 20px rgba(108, 99, 255, 0.3) !important;
    }
    .footer {
        text-align: center;
        color: #444;
        font-size: 0.82rem;
        padding-top: 1rem;
    }
    div[data-testid="stFileUploader"] {
        background: #0a0a0f !important;
        border: 2px dashed #2a2a3e !important;
        border-radius: 10px !important;
        padding: 0.5rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# Everything inside Streamlit container
with st.container():

    # Hero
    st.markdown("""
        <div class="hero">
            <div class="hero-badge">✨ AI POWERED</div>
            <div class="hero-title">AI Resume Analyzer</div>
            <div class="hero-subtitle">
                Get instant, detailed feedback on your resume 
                to help you land your dream job.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
        <div class="stats-container">
            <div class="stat-box">
                <div class="stat-number">10+</div>
                <div class="stat-label">Metrics Analyzed</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">ATS</div>
                <div class="stat-label">Compatibility Check</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">⚡</div>
                <div class="stat-label">Instant Results</div>
            </div>
        </div>
        <hr class="section-divider">
        <div class="upload-label">📎 Upload Your Resume (PDF)</div>
    """, unsafe_allow_html=True)

    # Upload
    uploaded_file = st.file_uploader("", type="pdf", label_visibility="collapsed")

    st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

    # Button
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
            st.markdown(f'<div class="result-box">{feedback}</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("""
        <hr class="section-divider">
        <div class="footer">
            Powered by Groq AI &nbsp;|&nbsp;
            <a href="https://github.com/tharunika-19/resume-analyzer" style="color:#6C63FF; text-decoration:none;">GitHub ↗</a>
        </div>
    """, unsafe_allow_html=True)