import openai
import json

class ChatGPTHandler:
    # APIキーのセット
    def __init__(self):
        with open('secret.json') as f:
            secret = json.load(f)
        openai.api_key = secret['KEY']
        
    # chatgptAPIとのやり取り
    def ans_chat_gpt(self, prompt,responses):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a cooking professional"},
                {"role": "user", "content": prompt}
            ],
            stream=True
        )

        response = ""
        for chunk in completion:
            if chunk:
                content = chunk['choices'][0]['delta'].get('content')
                if content:
                    response += content
                    responses[0] += content
                    yield response
