import os
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant name pragya  skilled in general tasks like alexa and google cloud."},
    {"role": "user", "content": "What is the capital of France?"}
  ]
)
print(response['choices'][0]['message']['content'])