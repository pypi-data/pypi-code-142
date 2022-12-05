import os
import sys
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def text_to_command(prompt):
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.2,
    presence_penalty=0.0,
  )

  return response

if __name__ == "__main__":
  if len(sys.argv) == 2:
    r = text_to_command(sys.argv[1])
    print(r['choices'][0]["text"])
