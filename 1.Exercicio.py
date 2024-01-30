
#1.Faça um Programa que mostre a mensagem "Alo mundo" na tela.
def pergunta_humor():
    resultado_humor = input("Digite o seu humor hoje - f (feliz) ou t (triste) ?")

    return resultado_humor

def responder_humor(resultado_humor):
    if resultado_humor == "f":
        print("oieee amor, tá dormindo?")
    elif resultado_humor == "t":
        print("Alô mundo")


responder_humor(pergunta_humor())





#Perguntar qual humor a pessoa está hoje (feliz(f) ou triste(t))
#se tiver feliz, diz "oieee mundo" 
#se tiver triste, diz "Alô mundo"
