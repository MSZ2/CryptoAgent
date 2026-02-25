import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-2.5-flash",
    #provider="google-genai",
    api_key=os.getenv("GOOGLE_API_KEY")
    
)

'''
groq_key = os.getenv("GROQ_API_KEY")

# Define the Groq LLM
gemini_llm = LLM(
    model="llama-3.3-70b-versatile",          # Pick a Groq model
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
    provider="openai"            # IMPORTANT
)
'''