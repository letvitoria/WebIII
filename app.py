from flask import Flask, render_template


app_Leticia = Flask(__name__, template_folder="t_templates")


@app_Leticia.route("/")
@app_Leticia.route("/index")
def index():
    nome_usuario = "Leticia"
    return render_template("t_index.html", nome=nome_usuario)


@app_Leticia.route("/contato")
def contato():
    return render_template("t_contato.html")


@app_Leticia.route("/usuario")
def dados_usuario():
    dados_usu = {
        "nome": "Leticia",
        "profissao": "Estudante",
        "disciplina": "Desenvolvimento Web III",
    }
    return render_template("usuario.html", dados=dados_usu)


if __name__ == "__main__":
    app_Leticia.run(port=7000, debug=True)
