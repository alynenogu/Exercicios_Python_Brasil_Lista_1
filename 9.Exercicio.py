#Faça um Programa que peça a temperatura em graus Fahrenheit,

#transforme e mostre a temperatura em graus Celsius.

#C = 5 * ((F-32) / 9).

def pergunta_temperatura_fahrenheit():
    temperatura_fahrenheit = int(input("Qual a temperatura em fahrenheit?"))
    return temperatura_fahrenheit

def calcula_para_celsius(temperatura):
    temperatura_celsius = 5 * ((temperatura-32) / 9)

    return print("A temperatura em Celsius é: ", temperatura_celsius)

fahrenheit = pergunta_temperatura_fahrenheit()
calcula_para_celsius(fahrenheit)
