from flask import flask, render_template

app = flask(__name__)

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

app.route("/servicos")
def servico():
    return render_template("servicos.html")

if __name__ == "__main__":
    app.run(debug=True)
