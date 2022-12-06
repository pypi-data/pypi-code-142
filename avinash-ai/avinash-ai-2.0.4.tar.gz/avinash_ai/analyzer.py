import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

# write a function to capture response from openai
def analyze_your_query(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
    return response.choices[0].text

