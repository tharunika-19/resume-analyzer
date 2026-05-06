def get_analysis_prompt(resume_text):
    return f"""
You are an expert resume reviewer and career coach.
Analyze the following resume and provide:

1. **Overall Score** (out of 10)
2. **Key Skills Found**
3. **Strengths** (what's good)
4. **Weaknesses** (what's missing)
5. **Improvement Suggestions** (specific actionable tips)
6. **ATS Friendliness** (will it pass applicant tracking systems?)

Resume:
{resume_text}

Be specific, honest and helpful.
"""