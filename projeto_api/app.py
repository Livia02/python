from itertools import count
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": 200, "message": "API de LIVIA_EDUARDA_SANTOS_CIRILO"})

@app.route("/aleatorios") # decorator de rotas
def aleatorios(): # função python
    import random
    a = random.randint(49, 100)
    return jsonify({"status": 200, "data": a})

@app.route("/argumentos/<string:nome>")
def argumentos(nome: str):
    return jsonify({"status": 200, "data": nome })

@app.route("/idades", methods=("GET, "))
def idades():
    from random_data import pessoas
    import funcoes
    num = funcoes.maior_de_50(pessoas)
    return jsonify({"status": 200, "data": num})

@app.route("/salarios", methods=("GET,"))
def salarios():
    from random_data import salarios
    import funcoes
    num = funcoes.mais_2000(salarios)
    return jsonify({"status": 200, "data": num })

@app.route("/maiores_salarios", methods=("GET,"))
def maiores_salarios():
    from random_data import maiores_salarios
    import funcoes
    num = funcoes.maior_salario(maiores_salarios)
    return jsonify({"status": 200, "data": num })

@app.route("/media_profissoes", methods=("GET,"))
def media_profissoes():
    from random_data import media_profissoes
    import funcoes
    num = funcoes.media_profissoes(media_profissoes)
    return jsonify({"status": 200, "data": num})

@app.route("/intervalo_idades_mais2000_sexo", methods=("GET, "))
def intervalo_idades_mais200_sexo():
    from random_data import intervalo_idades_mais2000_sexo
    import funcoes
    num = funcoes.maior_2000_sexo(intervalo_idades_mais2000_sexo)
    return jsonify({"status": 200, "data": num})
 
if __name__ == '_main_':
    app.run(debug=True)