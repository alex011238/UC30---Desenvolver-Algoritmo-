from flask import Flask, render_template, request, response

app = Flask(__name__)

@app.route("/")
def inicio():
    nome = request.get("nome")
    tema = request.get("tema", "claro", "escuro")

    return render_template("index.html", nome=nome, tema=tema)

@app.route("/salvar", methods=["POST"])
def salvar():
    nome = request.form.get("nome")
    tema = request.form.get("tema")

    resposta = response(render_template(
        "index.html",
        nome=nome,
        tema=tema
    ))

    resposta.set("nome", nome, max_age=60*60*24*30)
    resposta.set("tema", tema, max_age=60*60*24*30)

    return resposta

if __name__ == "__main__":
    app.run(debug=True)