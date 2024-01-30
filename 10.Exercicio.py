#Faça um Programa que peça a temperatura em graus Celsius, 
#transforme e mostre em graus Fahrenheit.

def pergunta_temperatura_celsius():
    temperatura_celsius = int(input("Qual a temperatura em Celsius? "))
    return temperatura_celsius

def calcula_para_fahrenheit(temperatura):
    resultado = temperatura * 9/5 + 32
    return print("A temperatura em Fahrenheit é: ", resultado)


temperatura = pergunta_temperatura_celsius()
calcula_para_fahrenheit(temperatura)