# pagina_para_ia
Este repositorio es para hacer una página sobre mi IA

```shell
curl http://localhost:11434/api/generate -d '{
  "model": "gemma3:1b",
  "prompt":"hola",
}
```

Este comando sirve para poder generar un mensaje
```shell
curl "https://api.groq.com/openai/v1/chat/completions" \
  -X POST \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer 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" \
  -d '{
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
         "stream": false,
         "stop": null
       }'
```


Codigo de Groq para Python: 

```python
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
```

  