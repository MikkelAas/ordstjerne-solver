from operator import eq
from flask import Flask, jsonify, make_response, request
from numpy import equal

from ordstjerneSolver import ordstjerne_solver

app = Flask(__name__)


@app.route('/solve', methods=['POST'])
def solve():
    content_type = request.headers.get('Content-Type')
    if (content_type != 'application/json'):
        return make_response('content type not supported', 400)

    body = request.get_json()

    all_letters: list = body['allLetters']
    special_letter: str = body['specialLetter']

    if (not isinstance(all_letters, list)
            or not isinstance(special_letter, str)
            or not isinstance(all_letters[0], str)
        ):
        return make_response({'error': 'json body does not match type'}, 400)

    word_list = ordstjerne_solver(all_letters, special_letter)

    total_word_amount = len(word_list)

    response = jsonify({
        'total': total_word_amount,
        'words':  word_list
    })

    return make_response(response, 200)
