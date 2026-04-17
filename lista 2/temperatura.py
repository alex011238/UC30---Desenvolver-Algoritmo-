
def ler_temperatura(indice):
    ("Lê uma temperatura do usuário com validação de entrada.")
    while True:
        try:
            valor = float(input(f"Digite a temperatura {indice} (em °C): "))
            return valor
        except ValueError:
            print("Entrada inválida! Digite um número válido (use ponto para decimais).")
