def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro! Divisão por zero."
    return a / b

def calculadora():
    print("=== CALCULADORA ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    while True:
        opcao = input("\nEscolha uma operação (1-5): ")

        if opcao == "5":
            print("Até logo!")
            break
        if opcao in ["1", "2", "3", "4"]:
            num1 = float(input("Digite o primeiro número:"))
            num2 = float(input("Digite o segundo  número:"))

            if opcao == "1":
                print(f"Resultado: {soma(num1,num2)}")
            elif opcao == "2":
                print(f"Resultado: {subtracao(num1,num2)})")
            elif opcao == "3":
                print(f"Resultado: {multiplicacao(num1,num2)}")
            elif opcao == "4":
                print(f"Resultado:{divisao(num1,num2)}")