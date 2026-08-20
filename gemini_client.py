import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()


def get_api_keys():
    """Load all available Gemini API keys from .env."""

    keys = []

    index = 1

    while True:
        key = os.getenv(f"GEMINI_API_KEY_{index}")

        if not key:
            break

        keys.append(key.strip())
        index += 1

    return keys


API_KEYS = get_api_keys()


if not API_KEYS:
    raise RuntimeError(
        "No Gemini API keys found. "
        "Add GEMINI_API_KEY_1 to your .env file."
    )


class GenerationError(Exception):
    pass


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

    last_error = None

    for index, api_key in enumerate(API_KEYS, start=1):

        try:
            print(f"Trying Gemini API key {index}...")

            # Create a fresh client using the current API key
            client = genai.Client(api_key=api_key)

            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
                config={
                    "response_mime_type": "application/json"
                }
            )

            if not response.text:
                raise GenerationError(
                    "Gemini returned an empty response."
                )

            try:
                data = json.loads(response.text)

                print(f"Gemini API key {index} succeeded.")

                return data

            except json.JSONDecodeError:
                raise GenerationError(
                    "Gemini returned invalid JSON."
                )

        except GenerationError:
            # Invalid JSON or empty response should not automatically
            # cause all keys to be tried.
            raise

        except Exception as e:

            last_error = str(e)

            print(
                f"Gemini API key {index} failed."
            )

            if index < len(API_KEYS):
                print("Trying backup API key...")
            else:
                print("No more API keys available.")

    raise GenerationError(
        f"All Gemini API keys failed. Last error: {last_error}"
    )
