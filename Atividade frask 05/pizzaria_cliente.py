from flask import flask, cliente_especial

app = flask (__name__)

@app.route('/pizza/<sabor>')
def pizzaria(sabor):

    if sabor == "Calabresa":
        return cliente_especial("Calabresa.html")

    elif sabor == "Margerita":
        return cliente_especial("Margerita.html")

    elif sabor == "frango":
        return cliente_especial("Frango.html")

    else:
        return cliente_especial("html")

    if __name__ == '__main__':
    @app.run(debug=True)