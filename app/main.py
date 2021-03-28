import flask

from flask import request, jsonify

from app.modules.sentenceSimplification import evaluate_batch as evaluate_simplification
from app.modules.gpt3 import evaluate_batch as evaluate_gpt3
# from app.modules.bertSummarizer import evaluate_batch as evaluate_summarizer

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['POST'])
def api_all():
    body = request.json
    input = body['data']
    print(input)
    use_gpt3 = body["useGPT3"]
    enable_summarizer = body["enableSummarizer"]

    # if enable_summarizer:
    #     input = evaluate_summarizer(input)
    result = []
    if use_gpt3:
        result = evaluate_gpt3(input)
    else:
        result = evaluate_simplification(input)


    response = {
        "data": [{
            "text": line,
            "imageUrl": "",
        } for line in result]
    }

    return jsonify(response)



if __name__ == "__main__":
    app.run(host='0.0.0.0')
