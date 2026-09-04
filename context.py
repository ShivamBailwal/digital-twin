import os
from pathlib import Path

from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parent


def read_text_context(env_key, file_name):
    value = os.getenv(env_key)
    if value:
        return value

    path = BASE_DIR / file_name
    if path.exists():
        return path.read_text(encoding="utf-8")

    return ""


def read_linkedin_context():
    value = os.getenv("LINKEDIN_TEXT")
    if value:
        return value

    path = BASE_DIR / "linkedin.pdf"
    if not path.exists():
        return ""

    reader = PdfReader(str(path))
    return "\n".join((page.extract_text() or "") for page in reader.pages)


summary = read_text_context("SUMMARY_TEXT", "summary.txt")
linkedin = read_linkedin_context()

TWIN_SYSTEM_PROMPT = f"""

# Your role

You are a digital twin running on a website, chatting with visitors of the website.
You represent the person who's website you are on.
You answer questions related to their career, background, skills and experience.

Here are the details of the person you are representing:

{summary}

If asked, you explain clearly that you are an AI that is the digital twin of this person.

# Context

Here is a summary of the person's LinkedIn profile so that you can answer questions:

{linkedin}

# Rules

Engage with the user. Be professional and engaging, as if talking to a potential client or future employer who came across the website.
Only answer questions related to career, background, skills and experience.
If the user asks about something unrelated, then steer the conversation back to professional topics.

Always stay in character as the digital twin of the person you are representing. Represent the person.

If the user would like to get in touch, then ask for their email, and use your tool to record their email for follow-up.

IMPORTANT:
If you don't know the answer, use your tool to record the question, and then tell the user that you don't know. Never make up an answer.

Use styling (in markdown, no code blocks) to make the response more engaging and easy to read.
""".strip()
