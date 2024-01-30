#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def pergunta_notas():
    primeira_nota = int(input("Digite a sua nota no primeiro bimestre? "))
    segunda_nota = int(input("Digite a sua nota no segundo bimestre? "))
    terceira_nota = int(input("Digite a sua nota no terceiro bimestre? "))
    quarta_nota = int(input("Digite a sua nota no quarto bimestre? "))

    return primeira_nota+segunda_nota+terceira_nota+quarta_nota

def media_notas(resultado):
    media = resultado/4

    return print("A média é ", media)

media_notas(pergunta_notas())