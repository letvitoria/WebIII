import os

from flask import Flask, flash, redirect, render_template, request, url_for


app_Leticia = Flask(__name__, template_folder="t_templates")
app_Leticia.config["SECRET_KEY"] = os.environ.get(
    "FLASK_SECRET_KEY", "chave-de-desenvolvimento-leticia"
)


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


# Versao 3: dados dinamicos recebidos diretamente pela URL.
@app_Leticia.route("/ola/<id>")
def saudacao(id):
    return render_template("t_index.html", nome=id)


@app_Leticia.route("/usuario/<nome>;<profissao>")
def dados_usuario_url(nome, profissao):
    dados_usu = {
        "nome": nome,
        "profissao": profissao,
        "disciplina": "Desenvolvimento Web III",
    }
    return render_template("usuario.html", dados=dados_usu)


# Versao 4: formularios com os metodos GET e POST.
@app_Leticia.route("/formulario", methods=["GET", "POST"])
def formulario():
    resultado = None
    if request.method == "POST":
        resultado = request.form.get("nome", "").strip()
        if resultado:
            flash(f"Formulario recebido, {resultado}!", "sucesso")
        else:
            flash("Informe seu nome para continuar.", "erro")
    else:
        resultado = request.args.get("nome", "").strip() or None
    return render_template("formulario.html", resultado=resultado)


@app_Leticia.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        senha = request.form.get("senha", "")
        if usuario == "admin" and senha == "1234":
            flash("Login realizado com sucesso.", "sucesso")
            return redirect(url_for("index"))
        flash("Usuario ou senha invalidos.", "erro")
    return render_template("login.html")


if __name__ == "__main__":
    app_Leticia.run(port=7000, debug=True)
