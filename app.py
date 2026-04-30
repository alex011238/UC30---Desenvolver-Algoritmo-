from flask import Flask, render_template_string

app = Flask(__name__)

alunos = [
    {"nome": "Luan", "matricula": 345555},  
    {"nome": "Ruan", "matricula": 122211},
    {"nome": "Juan", "matricula": 676767},
]


@app.route("/alunos")
def listar_alunos():
    return render_template_string(TABELA_HTML, alunos=alunos)

if __name__ == "__main__":
    app.run(debug=True)
