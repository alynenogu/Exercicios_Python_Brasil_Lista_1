#Faça um Programa que converta metros para centímetros.

def pergunta_metros():
    metros = int(input("Quantos metros deseja converter para cm?"))

    return metros

def converte_cm(metros):
    resultado = metros*100

    return print("O valor em cm é: ", resultado)


converte_cm(pergunta_metros())

