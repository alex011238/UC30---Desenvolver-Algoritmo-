def calcular_media():
    notas = []
    
    for i in range(3):
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))
            notas.append(nota)
        except ValueError:
            print("Erro: as notas devem ser numéricas.")
            return 
    
    media = sum(notas) / 3
    print(f"Média final: {media:.2f}")