from flask import Flask, session, redirect, url_for

app = Flask(__name__)

app.secret_key = 'chave_super_secreta_segura'

@app.route('/')
def contador_visitas():
    try:
        visitas = session.get('visitas', 0)
        visitas += 1  # Incrementa
        session['visitas'] = visitas

        return f"Você visitou este site {visitas} vezes."
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}", 500

@app.route('/reset')
def resetar_visitas():
    """Rota opcional para resetar o contador"""
    session.pop('visitas', None)
    return redirect(url_for('contador_visitas'))

if __name__ == '__main__':
    app.run(debug=True)
