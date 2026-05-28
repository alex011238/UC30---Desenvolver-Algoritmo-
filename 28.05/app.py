from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = '123'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'post':

        email = request.form.get('email')
        senha = request.form.get('senha')

        if not email or not senha:

            flash('Preencha todos os campos.', 'erro')
            return redirect(url_for('login'))

            if email != 'admin@gmail.com' or senha != "123":
                flash('E-mail ou senha inválido.', 'erro')
                return 