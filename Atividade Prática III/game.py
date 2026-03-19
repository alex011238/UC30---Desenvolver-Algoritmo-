def rank_jogador(pontos, derrotas):
    pontos_finais = pontos - (derrotas * 10)

    if pontos_finais < 0:
        return "Banido"

    elif pontos_finais < 100:
        return "Bronze" 
    elif pontos_finais < 300:
        return "Prata"
    elif pontos_finais < 600:
        return "Ouro"
    
    else:
        return "Diamante"
    

    def saldo_finais(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        taxa = saque * 0.02
        saque_total = saque + taxa
    else:
        saque_total = saque

        return saldo - saque_total
    
   def tipo_magia(fogo, agua):
    
    if fogo and agua:
        return "Vapor"
    elif fogo:
        return "Fogo"
    elif agua:
        return "Água"
    else:
        return "Sem magia"
    

tempo = input ("TEMPO E DIGITE")

def verificar_acesso(usuario, senha, tentativas):
    if tentativas >= 3:
        return "Bloqueado"
    elif usuario == "admin" and senha == "1234":
        return "Acesso total"
    elif usuario == "admin" and senha == "1234":
        return "Senha incorreta"
    else:
        return "Usuário inválido"


def lancar_foguete(combustivel, clima, sistema_ok):
    if combustivel < 100:
        return "Combustível insuficiente"
    elif clima == "bom":
        return "Clima desfavorável"
    elif sistema_ok == False
        return "Falha no sistema"
    else:
        return "Lançamento autorizado"
    
    
