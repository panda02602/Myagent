from openai import OpenAI
from TOOLS.tools import TOOLS
from dotenv import load_dotenv,find_dotenv
import os

load_dotenv(find_dotenv(), override=True)
client = OpenAI(
    api_key = os.getenv("API_KEY"),
    base_url = os.getenv("BASE_URL")
)


def llm(context:list):
    responses = client.chat.completions.create(
        model = "llama-3.1-8b-instant",
        messages = context,
        tools = TOOLS
    )
    return responses