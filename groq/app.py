import requests
import os

api_key = "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"
url = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

data = {
         "messages": [
           {
             "role": "user",
             "content": "hola"
           }
         ],
         "model": "deepseek-r1-distill-llama-70b",
         "temperature": 0.6,
         "max_completion_tokens": 4096,
         "top_p": 0.95,
         "stream": False
       }

response = requests.post(url, headers=headers, json=data)

print(response.text)