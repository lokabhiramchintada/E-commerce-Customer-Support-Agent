"""LLM client factory for A2A agents."""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


def create_llm() -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-lite",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.7,
    )
