import os

from flask import Flask, flash, redirect, render_template, request, session, url_for


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


usuarios_api = [
    {
        "nome": "Leticia",
        "profissao": "Estudante",
        "disciplina": "Desenvolvimento Web III",
    }
]


# Versao 7: API com leitura e cadastro de usuarios em memoria.
@app_Leticia.route("/api/usuarios", methods=["GET", "POST"])
def api_usuarios():
    if request.method == "GET":
        return {"usuarios": usuarios_api}

    novo_usuario = request.get_json(silent=True) or {}
    campos_obrigatorios = ("nome", "profissao", "disciplina")
    if any(not novo_usuario.get(campo) for campo in campos_obrigatorios):
        return {
            "erro": "Informe nome, profissao e disciplina."
        }, 400

    usuario = {
        campo: novo_usuario[campo].strip() for campo in campos_obrigatorios
    }
    usuarios_api.append(usuario)
    return usuario, 201


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
            session["usuario"] = usuario
            flash("Login realizado com sucesso.", "sucesso")
            return redirect(url_for("index"))
        flash("Usuario ou senha invalidos.", "erro")
    return render_template("login.html")


# Versao 8: sessao, rota protegida e encerramento do login.
@app_Leticia.route("/area-restrita")
def area_restrita():
    if "usuario" not in session:
        flash("Faça login para acessar esta área.", "erro")
        return redirect(url_for("login"))
    return render_template("area_restrita.html", usuario=session["usuario"])


@app_Leticia.route("/logout")
def logout():
    session.pop("usuario", None)
    flash("Logout realizado com sucesso.", "sucesso")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app_Leticia.run(port=7000, debug=True)
