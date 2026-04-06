import random

numero_ = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número entre 1 e 100!")

while True:
    palpite = int(input("Digite o usúaroi "))
    tentativas += 1

    if   numero:
        print("maior")
    elif numero:
        print("menor")
    else:
        print(f"Parabéns, Mano! Você acertou em tentativas.")
        break