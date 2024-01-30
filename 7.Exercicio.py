#Faça um Programa que calcule a área de um quadrado, 
#em seguida mostre o dobro desta área para o usuário.

def pergunta_lado():
    lado = int(input("Qual é o lado do quadrado: "))
    return lado

def calcula_area_quadrado(lado):
    return lado**2

def dobro_area(resultado):
    resultado_final = resultado *2
    
    return print("A área é: ", resultado, "O dobro da área é: ", resultado_final)

lado = pergunta_lado()
area = calcula_area_quadrado(lado)
dobro_area(area)