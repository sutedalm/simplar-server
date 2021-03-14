import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True


MOCK_DATA = {
    'data': ["How to avoid the",
             "dreaded public relations crisis",
             "Bob Pickard",
             "Opinion",
             "Most important, show communication of the leader",
             "F",
             "acebook is an example of a new public relations reality.",
             "Public relations means to manage communication:",
             "The communication between an organization and others.",
             "When something goes wrong for a company, everyone looks to the leader.",
             "When the leader is gone, or the leader has nothing to say,",
             "no information is there. This is called an information vacuum.",
             "When an information vacuum happens, people on social media say,",
             "the company is wrong. If this happens, these people are in the centre",
             "of public relations. The opinion of these people suddenly",
             "becomes a general wisdom."]
}


@ app.route('/', methods=['GET'])
def index():
    return "<h1>Hello World</h1>"


@ app.route('/api', methods=['POST'])
def api_all():
    # body = request.json
    # print(body)
    # return jsonify(body['data'])
    return jsonify(MOCK_DATA)


if __name__ == "__main__":
    app.run()
