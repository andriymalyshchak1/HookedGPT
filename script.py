"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
print("GOOGLE_API_KEY:", os.getenv("GOOGLE_API_KEY"))

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found in environment variables")

genai.configure(api_key=api_key)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 2048,
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash-latest",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)
print(chat_session.history)
