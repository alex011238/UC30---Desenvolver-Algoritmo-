notas = [7.5, 8,0, 9.5, 6.0, 8.5]
print("Notas: ", notas)

print("Menor: ", min(notas))
print("Maior: ", max(notas))
print("soma: ", sum(notas))
print("Média: ", sum(notas) / (lennotass))

nomes = ["Adriana", "Breno", "Carla", "Daniel"]

print("Usando FOR simples: ")
for nome in nomes:
    print(f"Olá, {nome}!")

    print("\n Usando enumerate: ")
    for indice, nome in enumerate(nomes):
        print(f"Posição {indice}: {nome}")

        
