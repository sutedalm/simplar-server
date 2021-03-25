
from summarizer import Summarizer

print("initializing bert summarizer")
model = Summarizer()
print("finished initializing bert summarizer")

def evaluate(input: str) -> str:
  return model(line)

def evaluate_batch(input: [str]) -> [str]:
  return list(map(evaluate, input))
