from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

# Initialize Gemini
llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

def ask_mentor(question):
    """
    AI Mentor Chatbot
    Takes a user question and returns only plain text.
    """

    prompt = f"""
You are an expert AI Learning Mentor.

Your job is to teach students in a simple, beginner-friendly way.

Rules:
- Answer in simple English.
- Explain step by step.
- Use examples whenever possible.
- If the topic is programming, include code examples.
- If the question is about AI/ML, explain the concepts clearly.
- If the question is unrelated, politely answer it if possible.
- Return ONLY plain text. Do NOT return JSON, markdown objects, or dictionaries.

Student Question:
{question}
"""

    try:
        response = llm.invoke(prompt)

        # Extract plain text from response
        if hasattr(response, "text") and response.text:
            return response.text

        if isinstance(response.content, str):
            return response.content

        if isinstance(response.content, list):
            text = ""
            for block in response.content:
                if isinstance(block, dict):
                    text += block.get("text", "")
                else:
                    text += str(block)
            return text.strip()

        return str(response.content)

    except Exception as e:
        error = str(e)

        if "quota" in error.lower():
            return "❌ Gemini API quota exceeded."

        elif "API_KEY_INVALID" in error or "API key not valid" in error:
            return "❌ Invalid Gemini API Key."

        elif "429" in error:
            return "❌ Too many requests. Please try again later."

        else:
            return f"❌ Error: {error}"