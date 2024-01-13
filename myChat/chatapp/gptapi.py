import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine="whisper-1",  # Use the appropriate engine for your needs
    prompt="Tell me a joke.",
    max_tokens=500  # Adjust as needed
)

generated_text = response.choices[0].text
print(generated_text)
