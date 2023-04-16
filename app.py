from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'title': 'O Senhor dos Anéis',
        'Autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'title': 'Harry Potter e a pedra Filosofal',
        'Autor': 'J.K Howling'
    },
    {
        'id': 3,
        'title': 'Interestelar',
        'Autor': 'Norlan'
    }
]

# Consultar(todos) / GET 
@app.route('/livros', methods=['GET'])
def obter_livros(): 
    return jsonify(livros)

# Consultar(id) 
@app.route('/livros/<int:id>',methods=['GET']) 
def obter_livros_por_id(id):    
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
#Editar
@app.route('/editar/livros/<int:id>',methods=['PUT']) 
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros): # indice seria o [0] de uma array
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

# Criar
@app.route('/livros',methods=['POST']) 
def criar_novo_livro():
    novo_livro = request.get_json() # request.get_json(), usa-se essa expressão para mexer no body
    livros.append(novo_livro)

    return jsonify(livros)

# Excluir
@app.route('/livros/<int:id>',methods=['DELETE']) 
def deletar_livro(id):
     for indice, livro in enumerate(livros):
         if livro.get('id') == id:
             del livros[indice]

    return jsonify(livros)

app.run(port=5000, host="localhost", debug=True)