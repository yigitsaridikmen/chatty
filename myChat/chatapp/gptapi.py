import openai
import os
from openai import OpenAI

OPENAI_API_KEY='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'

client = OpenAI(api_key=OPENAI_API_KEY)
def gptBot(prompter,message):
    print('GPT IS TRIGGERED')
    completion  = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}],
    )
    response = completion.choices[0].message.content
    return response
