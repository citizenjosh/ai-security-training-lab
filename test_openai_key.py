import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

try:
    models = client.models.list()
    print("✅ OpenAI API Key is valid!")
except Exception as e:
    print("❌ Error:", e)
