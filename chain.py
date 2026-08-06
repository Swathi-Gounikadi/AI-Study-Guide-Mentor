from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langfuse import observe

import prompt
from parser import LearningPath

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="models/gemini-flash-latest",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.7,
)

structured_llm = llm.with_structured_output(LearningPath)

chain = prompt.prompt | structured_llm


@observe()
def generate_learning_path(user_input):
    return chain.invoke(
        {
            "skill": user_input.skill,
            "level": user_input.level,
            "goal": user_input.goal,
            "style": user_input.style,
        }
    )