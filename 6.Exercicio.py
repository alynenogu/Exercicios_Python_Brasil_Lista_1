#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi


def pergunta_raio_circulo():
    raio = int(input("Qual é o raio do círculo? "))
    return raio

def calcula_area_circulo(raio):
    resultado = pi*(raio**2)
    return  resultado


raio = (pergunta_raio_circulo())
resultado_final = calcula_area_circulo(raio)
print("A área do círculo é:",resultado_final)