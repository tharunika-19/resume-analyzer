from groq import Groq
from app.prompts import get_analysis_prompt

def analyze_resume(resume_text, api_key):
    client = Groq(api_key=api_key)
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": get_analysis_prompt(resume_text)
            }
        ]
    )
    
    return response.choices[0].message.content