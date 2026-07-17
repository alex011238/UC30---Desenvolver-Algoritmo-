from flask import flask, render_template, request,
redirect, url_for
import json
import os

  def carregar_filmes():
    """ Lê o arquivo Json e retorna uma lista de filmes. """

    if not os.path.exists(ARQUIVOS):
        return []

    with open(ARQUIVOS, "r", encoding="utf-8") as arquivo:
        try:
            return json.load(arquivo)
        except json.JSONDecodeError:
            return []


  def salvar_filmes(lista_filmes):
    """Salvar a lista de filmes no arquivo JSON."""

    with open(ARQUIVO, "W", encoding)
    

     
  

    
    @app.route("/", methods=["GET" "POST"])
    def cadastro():

        if request.method == "POST":

            filme = { 
                "Nome": request.form["nome"]
                "genro": request.form["genro"]
                "ano": request.form["ano"]
            }

            filmes = carregar_fillmes()
            filmes.append(filme)
            salvar_filmes(filmes)

            return redirect(url_for("listar"))

        return render_template("cadastro.html")
            
    app.route("/filmes")
    def listar():

        filmes = carregar_filmes()

        return render_template(
            "filmes.html",
            filmes=filmes
        )

if __name__ == "__main__":
    app.run(debug=True)