from flask import Flask, render_template


app_Leticia = Flask(__name__, template_folder="t_templates")


@app_Leticia.route("/")
@app_Leticia.route("/index")
def index():
    return render_template("t_index.html")


@app_Leticia.route("/contato")
def contato():
    return render_template("t_contato.html")


if __name__ == "__main__":
    app_Leticia.run(port=7000, debug=True)
