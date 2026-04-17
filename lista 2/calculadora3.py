def contar_vogais(texto):
    input = ("Qual é sua vogais")
vogais = ['a', 'e', 'i', 'o', 'u']
count_vogais = 0
for letra in texto.lower():

if letra in vogais:
count_vogais += 1
print("f'A frase possui {count_vogais} vogais.")