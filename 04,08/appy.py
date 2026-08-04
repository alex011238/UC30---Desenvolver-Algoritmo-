from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "senha_super_secreta"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        usuario = request.form["usuario"]
        senha = request.form["senha"]

        if usuario == "admin" and senha == "123":

            session["usuario"] = usuario
            return redirect(url_for("painel"))

    return render_template("login.html")

@app.route("/painel")
def painel():

    if "usuario" not in session:
        return redirect(url_for("login"))

    return render_template("painel.html", usuario=session["usuario"])

@app.route("/logout")
def logout():

    session.pop("usuario", None)

    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)