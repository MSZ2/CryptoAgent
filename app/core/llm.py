import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()
gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    #provider="google-genai",
    api_key=os.getenv("GOOGLE_API_KEY")
    
)
