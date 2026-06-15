from flask import Flask, session, request, render_template_string

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        cor_favorita = request.form.get('cor_favorita')
        if cor_favorita:
            session['cor_favorita'] = cor_favorita

    cor = session.get('cor_favorita', 'nenhuma')
    
    html = '''
    <h1>Cor favorita do usuário</h1>
    <p>Sua cor favorita armazenada é: {{ cor }}</p>
    <form method="POST">
        <label>Digite sua cor favorita:</label>
        <input type="text" name="cor_favorita" required>
        <button type="submit">Salvar</button>
    </form>
    '''
    return render_template_string(html, cor=cor)

if __name__ == '__main__':
    app.run(debug=True)