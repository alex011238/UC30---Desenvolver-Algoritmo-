from flask import flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def produtos():

    with open("produtos", "r", encoding="utf-8") as arquivos:
        lista_produtos = json.load(arquivos)

    return render_template("produto.html", produtos=listas_produtos)

if __name = '__main__':
    app.run(debug=True)