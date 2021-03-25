
import openai
import os

def evaluate(input: str) -> str:
    intro = "My second grader asked me what this passage means:\n\"\"\"\n"
    outro = "\n\"\"\"\nI rephrased it for him, in plain language a second grader can understand:\n\"\"\"\n"
    openai.api_key = os.environ["GPT3_KEY"]
    response = openai.Completion.create(
    engine="davinci",
    prompt=intro + input + outro,
    temperature=0,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
    )

    return response["choices"][0]["text"]

def evaluate_batch(input: [str]) -> [str]:
  return list(map(evaluate, input))
