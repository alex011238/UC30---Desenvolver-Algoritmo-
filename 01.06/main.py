from 

print("=== Sistema de Inscrição para Campeonato de Games ===")

nickname = input("Digite seu nickname: ")
jogo = input("Digite o jogo escolhido: ")
email = input("Digite seu e-mail: ")

if nickname == "" or jogo == "" or email == "":
    print("Preencha todos os campos obrigatórios.")

elif len(nickname) < 4:
    print("Preencha todos os campos obrigatórios.")

else:
    print("Inscrição realizada com sucesso!")