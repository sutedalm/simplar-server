import flask

from flask import request, jsonify

from access.preprocessors import get_preprocessors
from access.resources.prepare import prepare_models
from access.simplifiers import get_fairseq_simplifier, get_preprocessed_simplifier
from access.text import word_tokenize
from access.utils.helpers import yield_lines, write_lines, get_temp_filepath, mute
import os
import openai

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# A route to return all of the available entries in our catalog.


@app.route('/', methods=['POST'])
def api_all():
    body = request.json
    print(body['data'])
    input = body['data']
    ai = body["ai"]
    result = []
    if ai == True:
        result = [gpt3(line) for line in input]
    else:
        result = evaluate(input)

    return jsonify(result)


def evaluate(input):
    # Usage: python generate.py < my_file.complex
    # Read from stdin
    source_filepath = get_temp_filepath()
    write_lines([word_tokenize(line) for line in input], source_filepath)

    # Load best model
    best_model_dir = prepare_models()
    recommended_preprocessors_kwargs = {
        'LengthRatioPreprocessor': {'target_ratio': 0.95},
        'LevenshteinPreprocessor': {'target_ratio': 0.75},
        'WordRankRatioPreprocessor': {'target_ratio': 0.75},
        'SentencePiecePreprocessor': {'vocab_size': 10000},
    }

    preprocessors = get_preprocessors(recommended_preprocessors_kwargs)
    simplifier = get_fairseq_simplifier(best_model_dir, beam=8)
    simplifier = get_preprocessed_simplifier(simplifier, preprocessors=preprocessors)
    # Simplify
    pred_filepath = get_temp_filepath()

    with mute():
        simplifier(source_filepath, pred_filepath)

    return [line for line in yield_lines(pred_filepath)]


def gpt3(input):
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


if __name__ == "__main__":
    app.run()
