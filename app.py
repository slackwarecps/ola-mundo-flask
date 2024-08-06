from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h1>Olá Mundo! Sou uma app flask rodando no docker!!!</h2>'


if __name__ == "__main__":
    # o container docker esta soltando a app na porta 5011!!!! 
    app.run(debug=True)