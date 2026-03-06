from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World!!!</h1>"


@app.route("/curso")
def curso():
    return "<h1>Curso de DEV</h1>"

@app.route("/cidade")
def cidade():
    dados = {
        "nome": "Piracicaba",
        "estado": "SP", 
        "populacao": 423000
        

    }
    return dados

if __name__ == "__main__":
    app.run(debug=True)