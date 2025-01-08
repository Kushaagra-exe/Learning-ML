import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv(c)

groq_key =  os.getenv('GROQ_API')

ChatGroq(model="gemma2-9b-it", groq_api_key=groq_key)

