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
    
    .main { background-color: #0a0a0f; }
    
    .hero {
        text-align: center;
        padding: 3rem 2rem 2rem 2rem;
    }
    
    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, #6C63FF22, #FF658422);
        border: 1px solid #6C63FF55;
        color: #6C63FF;
        padding: 0.4rem 1rem;
        border-radius: 50px;
        font-size: 0.85rem;
        font-weight: 600;
        margin-bottom: 1.5rem;
        letter-spacing: 1px;
    }
    
    .hero-title {
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #ffffff 0%, #6C63FF 50%, #FF6584 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        line-height: 1.2;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        color: #888;
        font-size: 1.1rem;
        max-width: 500px;
        margin: 0 auto 2rem auto;
        line-height: 1.6;
    }
    
    .card {
        background: linear-gradient(145deg, #13131f, #1a1a2e);
        border: 1px solid #2a2a3e;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(108, 99, 255, 0.1);
    }
    
    .card-title {
        color: #ffffff;
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    .result-card {
        background: linear-gradient(145deg, #13131f, #1a1a2e);
        border: 1px solid #6C63FF44;
        border-radius: 20px;
        padding: 2.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 8px 32px rgba(108, 99, 255, 0.15);
    }
    
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #6C63FF, #FF6584) !important;
        color: white !important;
        border: none !important;
        padding: 0.85rem 2rem !important;
        border-radius: 12px !important;
        font-size: 1.05rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 20px rgba(108, 99, 255, 0.3) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(108, 99, 255, 0.5) !important;
    }
    
    .footer {
        text-align: center;
        color: #444;
        font-size: 0.85rem;
        padding: 2rem 0;
    }
    
    .stat-row {
        display: flex;
        gap: 1rem;
        margin-bottom: 1.5rem;
    }
    
    .stat-box {
        flex: 1;
        background: #0a0a0f;
        border: 1px solid #2a2a3e;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    
    .stat-number {
        font-size: 1.8rem;
        font-weight: 800;
        color: #6C63FF;
    }
    
    .stat-label {
        font-size: 0.75rem;
        color: #666;
        margin-top: 0.2rem;
    }

    div[data-testid="stFileUploader"] {
        background: #0a0a0f;
        border: 2px dashed #2a2a3e;
        border-radius: 12px;
        padding: 1rem;
    }
    
    div[data-testid="stFileUploader"]:hover {
        border-color: #6C63FF;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
    <div class="hero">
        <div class="hero-badge">✨ AI POWERED</div>
        <div class="hero-title">AI Resume Analyzer</div>
        <div class="hero-subtitle">
            Get instant, detailed feedback on your resume. 
            Powered by advanced AI to help you land your dream job.
        </div>
    </div>
""", unsafe_allow_html=True)

# Stats row
st.markdown("""
    <div class="stat-row">
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
""", unsafe_allow_html=True)

# Upload Card
st.markdown('<div class="card"><div class="card-title">📎 Upload Your Resume</div>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type="pdf", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

# Analyze Button
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
        
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.markdown(feedback)
        st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class="footer">
        Built with ❤️ by Tharunika &nbsp;|&nbsp; Powered by Groq AI &nbsp;|&nbsp; 
        <a href="https://github.com/tharunika-19/resume-analyzer" style="color: #6C63FF;">GitHub</a>
    </div>
""", unsafe_allow_html=True)