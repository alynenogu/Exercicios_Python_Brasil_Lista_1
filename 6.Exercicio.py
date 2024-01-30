#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

from math import pi


def pergunta_raio_circulo():
    raio = int(input("Qual é o raio do círculo? "))
    return raio

def calcula_area_circulo(raio):
    resultado = raio * pi
    return print("A área é: ", resultado)


calcula_area_circulo(pergunta_raio_circulo())