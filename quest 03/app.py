from flask import Flask, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave-secreta-bem-segura"

@app.route('/logout')
def logout():
    session.clear()
    
    flash("Você saiu da sua conta com sucesso!", "info")
    
    return redirect(url_for('index'))

@app.route('/')
def index():
    return "Página inicial - faça login para continuar."

if __name__ == '__main__':
    app.run(debug=True)
