#João Papo-de-Pescador, homem de bem,
#comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento
#de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo 
#excedente. João precisa que você faça um programa que leia a variável peso 
#(peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos 
#além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

def pergunta_qtd_peixe():
    qtd_peixes = float(input("Quantos quilos de peixe (em KG)?"))
    return qtd_peixes
def verifica_excesso(qtd_peixes):
    if qtd_peixes > 50:
       Flag_excesso = True
       return Flag_excesso
    elif qtd_peixes < 50:
       Flag_excesso = False
       return Flag_excesso
    

def calcula_excesso(Flag_excesso,qtd_peixes):
    if Flag_excesso ==True:
       resultado = qtd_peixes - 50
       return resultado
    elif Flag_excesso ==False:
        resultado =0
        return resultado

def calcula_multa(resultado):
    reais_excesso = resultado * 4

    return reais_excesso


resposta_quilos = pergunta_qtd_peixe()
flag = verifica_excesso(resposta_quilos)
resposta = calcula_excesso(flag,resposta_quilos)
resultado_final  = calcula_multa(resposta)
print("Peso em excesso: ", resposta)
print("O valor que deverá ser pago em excesso: R$", resultado_final)




    