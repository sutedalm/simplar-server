
from summarizer import Summarizer

model = Summarizer()

def evaluate(input: str) -> str:
  return model(line)

def evaluate_batch(input: [str]) -> [str]:
  return list(map(evaluate, input))
