#Faça um Programa que converta metros para centímetros.

def pergunta_metros():
    metros = int(input("Quantos metros deseja converter para cm?"))

    return metros

def converte_cm(metros):
    resultado = metros*100

    return resultado


valor_metros = pergunta_metros()
resultado_cm = converte_cm(valor_metros)

print("O valor em cm é: ", resultado_cm)

