from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():

    nome = request.form.get('nome', '').strip()
    idade = request.form.get('idade', '').strip()
    email = request.form.get('email', '').strip()

    erros = []

    if not nome:
        erros.append("O nome é obrigatório.")
    try:
        idade = int(idade)
        if idade < 0:
            erros.append("A idade não pode ser negativa.")
    except ValueError:
        erros.append("A idade deve ser um número inteiro.")

    if '@' not in email or '.' not in email:
        erros.append("E-mail inválido.")

    nome = nome.title()
    email = email.lower()

    if erros:
        return render_template(
            'resultado.html',
            erros=erros
        )

    return render_template(
        'resultado.html',
        nome=nome,
        idade=idade,
        email=email,
        erros=None
    )

if __name__ == '__main__':
    app.run(debug=True)