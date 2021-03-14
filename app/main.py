import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# A route to return all of the available entries in our catalog.


@app.route('/', methods=['GET'])
def index():
    return "<h1>Hello World</h1>"


@app.route('/api', methods=['POST'])
def api_all():
    body = request.json
    print(body)
    return jsonify(body['data'])


if __name__ == "__main__":
    app.run()
