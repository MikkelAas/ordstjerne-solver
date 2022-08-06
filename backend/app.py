from flask import Flask, jsonify, make_response, request

from flask_cors import CORS

from ordstjerneSolver import ordstjerne_solver

app = Flask(__name__)
CORS(app)


@app.route('/solve', methods=['POST'])
def solve():
    content_type = request.headers.get('Content-Type')

    if (content_type != 'application/json'):
        return make_response('content type not supported', 400)

    body = request.get_json()

    letters: list = body['letters']
    special_letter: str = body['specialLetter']

    # check types
    if (not isinstance(letters, list)
                or not isinstance(special_letter, str)
                or not isinstance(letters[0], str)
            ):
        return make_response({'error': 'json body does not match type'}, 400)

    if (len(letters) != 7):
        return make_response({'error': 'letters should be exactly 7 entries long'}, 406)

    # Solve the word puzzle
    word_list = ordstjerne_solver(letters, special_letter)

    total_word_amount = len(word_list)

    response = jsonify({
        'total': total_word_amount,
        'words':  word_list
    })

    return make_response(response, 200)
