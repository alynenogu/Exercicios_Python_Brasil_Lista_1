#Tendo como dados de entrada a altura de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, 
#usando a seguinte fórmula: (72.7*altura) - 58

def pergunta_altura():
    altura = float(input("Digite a altura :"))
    return altura

def calcula_peso_ideal(altura):
    resultado = (72.7*altura) - 58

    return  resultado 

altura_informada = pergunta_altura()
resultado = calcula_peso_ideal(altura_informada)
print("O peso ideal é: ",resultado)