import openai
import os
from openai import OpenAI

OPENAI_API_KEY='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'
# def gptBot(prompter,message):
#     response = openai.Completion.create(
#         engine="gpt-3.5-turbo",  # Use the appropriate engine for your needs
#         prompt=message,
#         max_tokens=500  # Adjust as needed
# )
#     generated_text = response.choices[0].text
#     print('GPTs response:',generated_text,' END')
#     return generated_text


client = OpenAI(api_key=OPENAI_API_KEY)
def gptBot(prompter,message):
    print('GPT IS TRIGGERED')
    completion  = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": message}],
    )
    response = completion.choices[0].message.content
    return response
