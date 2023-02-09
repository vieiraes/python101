from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Titulo de livro',
        'autor': 'Bruno Vieria'
    },
    {
        'id': 2,
        'titulo': 'Titulo 2',
        'autor': 'Bruno Vieria'
    },
    {
        'id': 3,
        'titulo': 'Titulo 3',
        'autor': 'Bruno Vieria'
    }
]


@app.route('/livros', methods=['GET', 'POST'])
def get_livros():
    if request.method == 'GET':
        return jsonify(livros)
    elif request.method == 'POST':
        novo_livro = request.get_json()
        livros.append(novo_livro)
        return jsonify(livros), 201


@app.route('/livros/<int:id>', methods=['GET'])
def get_books_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)


app.run(port=5000, host='localhost', debug=True)
