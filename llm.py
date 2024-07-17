# -*- coding: utf-8 -*-
"""LLM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R1AzhWktjJ53yZ4ywJ7Mwm6XtCKz61Bc
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_mistralai.chat_models import ChatMistralAI
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import os

with open('.env', 'w') as f:
    f.write("""
GOOGLE_API_KEY = "google_api_key"
ANTHROPIC_API_KEY = "anthropic_api_key"
MISTRALAI_KEY = "mistralali_api_key"
GROQ_API_KEY = "groq_api_key"
    """)

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
MISTRALAI_KEY = os.getenv("MISTRALAI_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

gemini_model = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key = GOOGLE_API_KEY)
claude_model = ChatAnthropic(model='claude-3-opus-20240229', api_key=ANTHROPIC_API_KEY, temperature=0)
mistral_ai_model = ChatMistralAI(api_key=MISTRALAI_KEY)
llama3_8b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama3-8b-8192")
mixtral_8x7b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")
llama3_70b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="llama3-70b-8192")
gemma_7b_model = ChatGroq(temperature=0, groq_api_key=GROQ_API_KEY, model_name="gemma-7b-it")

def gemini_response(prompt):
    response = gemini_model.invoke(prompt)
    return response.content

def claude_response(prompt):
    response = claude_model.invoke(prompt)
    return response.content

def mistral_ai_response(prompt):
    response = mistral_ai_model.invoke(prompt)
    return response.content

def llama3_8b_response(prompt):
    response = llama3_8b_model.invoke(prompt)
    return response.content

def mixtral_8x7b_response(prompt):
    response = mixtral_8x7b_model.invoke(prompt)
    return response.content

def llama3_70b_response(prompt):
    response = llama3_70b_model.invoke(prompt)
    return response.content

def gemma_7b_response(prompt):
    response = gemma_7b_model.invoke(prompt)
    return response.content

model_functions = {
    "Google AI's Gemini": gemini_response,
    "Anthropic's Claude": claude_response,
    "Mistral AI": mistral_ai_response,
    "LLaMA 3 8B": llama3_8b_response,
    "Mixtral 8x7B": mixtral_8x7b_response,
    "LLaMA 3 70B": llama3_70b_response,
    "Gemma 7B": gemma_7b_response,
}
