from flask import Flask, render_template

app = Flask(__name__)

@app.route('/arearestrita/<id>')
def area_restrita(id):
    if id == "aberto":
        mensagem = "Cadeado Aberto"
    else:
        mensagem = "Cadeado Fechado"
    
    return render_template('arearestrita.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)