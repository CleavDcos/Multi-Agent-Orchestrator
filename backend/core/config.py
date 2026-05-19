#every code can import env from here rather then writing it in every file, thus make code clean
from dotenv import load_dotenv
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

