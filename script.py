"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai
def get_gemini_response(prompt):
  load_dotenv()

  api_key = os.getenv("GOOGLE_API_KEY")
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
      
  )
  user_input = input("Send a question: ")
  response = chat_session.send_message(user_input)
  print(response.text)
  return response.text
