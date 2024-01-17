import openai
import os
from openai import OpenAI

OPENAI_API_KEY='API Key is hidden due to security concerns'

client = OpenAI(api_key=OPENAI_API_KEY)
def gptBot(prompter,message):
    completion  = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}],
    )
    response = completion.choices[0].message.content
    return response
