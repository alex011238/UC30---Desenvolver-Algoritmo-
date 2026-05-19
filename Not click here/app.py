from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html')

@app.route('/lanche')
def lanche():
    return render_template('lanche.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')

@app.route('/cliente')
def cliente():
    return render_template('cliente.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)