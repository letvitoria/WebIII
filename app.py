from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Olá, turma! Meu servidor Flask está rodando!"

@app.route('/ola')
def ola():
    return "Olá, esta é a página de boas-vindas (/ola)!"

if __name__ == '__main__':
    app.run(debug=True)