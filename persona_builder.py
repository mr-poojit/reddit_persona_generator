import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

TEMPLATE = """
You're an expert persona builder. Analyze this user's Reddit posts and comments and generate a persona including:

- Interests
- Personality Traits
- Writing Style
- Beliefs / Opinions
- Common Themes

For each point, cite the specific post or comment that supports your conclusion (include short quote and URL).

Reddit Data:
{data}
"""

def build_persona(username, items):
    prompt_data = "\n\n".join([
        f"[{item['type'].capitalize()}] {item['text'][:300]}...\nURL: {item['url']}"
        for item in items
    ])

    full_prompt = TEMPLATE.format(data=prompt_data)
    response = model.generate_content(full_prompt)
    return response.text
