from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)

ARQUIVO = "livros.json"

def carregar_livros():
    if not os.path.exists(ARQUIVO):
        with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
            json.dump([], arquivo)

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_livros(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(livros, arquivo, ensure_ascii=False, indent=4)


@app.route("/", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":
        titulo = request.form["titulo"].strip()
        autor = request.form["autor"].strip()
        ano = request.form["ano"].strip()

        # Validação dos campos
        if not titulo or not autor or not ano:
            return "Todos os campos são obrigatórios!"

        if not ano.isdigit():
            return "O ano deve conter apenas números!"

        livros = carregar_livros()

        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano
        }

        livros.append(livro)
        salvar_livros(livros)

        return redirect(url_for("listar_livros"))

    return render_template("cadastro.html")


@app.route("/livros")
def listar_livros():
    livros = carregar_livros()
    return render_template("livros.html", livros=livros)


@app.route("/excluir/<int:id>")
def excluir(id):
    livros = carregar_livros()

    if 0 <= id < len(livros):
        livros.pop(id)
        salvar_livros(livros)

    return redirect(url_for("listar_livros"))


if __name__ == "__main__":
    app.run(debug=True)