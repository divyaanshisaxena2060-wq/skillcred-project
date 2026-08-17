import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)


class GenerationError(Exception):
    pass


def resume_text_to_portfolio_data(resume_text):
    prompt = f"""
You are an AI portfolio generator.

Analyze the resume below and extract all available information.

Return ONLY valid JSON.
Do not write any explanation before or after the JSON.
Do not use Markdown.
Do not use ```json or ```.

Use exactly this structure:

{{
    "name": "",
    "about": "",
    "skills": [],
    "education": [],
    "projects": [],
    "experience": [],
    "certifications": [],
    "contact": {{
        "email": "",
        "phone": ""
    }},
    "social_links": {{
        "linkedin": "",
        "github": "",
        "portfolio": ""
    }}
}}

Important:
- Extract information from the resume accurately.
- Do not invent information.
- If information is not available, use an empty string or empty array.
- Include ALL projects mentioned in the resume.
- Include ALL skills mentioned in the resume.
- Include ALL education details.
- Include ALL certifications.
- Include email, phone, LinkedIn and GitHub if present.

Resume:
{resume_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        if not response.text:
            raise GenerationError("Gemini returned an empty response")

        try:
            return json.loads(response.text)

        except json.JSONDecodeError:
            raise GenerationError("Gemini returned invalid JSON")

    except GenerationError:
        raise

    except Exception as e:
        raise GenerationError(f"Gemini API error: {e}")

