from flask import Flask, session, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave-secreta-bem-segura"  # Necessário para usar session e flash

@app.route('/logout')
def logout():
    # Limpa todos os dados da sessão
    session.clear()
    
    # Mensagem para o usuário
    flash("Você saiu da sua conta com sucesso!", "info")
    
    # Redireciona para a página inicial
    return redirect(url_for('index'))

@app.route('/')
def index():
    return "Página inicial - faça login para continuar."

if __name__ == '__main__':
    app.run(debug=True)
