import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="Write an email to my boss for resignation?",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)