from flask import Flask, request, jsonify

from match.index import player_index
from match import find

app = Flask(__name__)


@app.after_request
def set_access(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add(
        'Access-Control-Allow-Headers', 'Content-type, Authorization'
    )
    response.headers.add(
        'Access-Control-Allow-Methods', 'POST, GET, PUT, DELETE'
    )
    return response


@app.route('/match', methods=['POST'])
def match():
    matched = find(request.form['name'])
    return jsonify(matched)


@app.route('/index', methods=['GET'])
def index():
    return jsonify(list(player_index.keys()))


if __name__ == '__main__':
    app.run()
