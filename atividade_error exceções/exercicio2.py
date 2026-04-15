def calcular_total_compra():
    
    try:
        preco1 = float(input("Digite o preço do primeiro produto: "))
        preco2 = float(input("Digite o preço do segundo produto: "))
        
        total = preco1 + preco2
        print(f"Total da compra: R$ {total:.2f}")
    
    except ValueError:
        print("Erro: os preços devem ser numéricos.")
        return 