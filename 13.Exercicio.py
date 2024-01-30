#Tendo como dado de entrada a altura (h) de uma pessoa, 
#construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

def pergunta_altura():
    altura = float(input("Qual é sua altura? "))
    

    return altura 

def pergunta_genero():
   
    genero = input("Qual é seu gênero? Selecione f para feminino e m para masculino")

    return  genero

def calcula_peso_ideial(altura, genero):
    
    if genero == "f": 
        resultado  = (62.1*altura) - 44.7
        return print("O seu peso ideal é: ", resultado)
    elif genero == "m":
        resultado = (72.7*altura) - 58
        return print("O seu peso ideal é: ", resultado)

altura_informada = pergunta_altura()
genero_informado = pergunta_genero()

calcula_peso_ideial(altura_informada,genero_informado)