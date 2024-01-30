#Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês.

def pergunta_ganho_hora():
    ganho_hora = int(input("Qual é o valor da hora de trabalho? "))
    return ganho_hora

def horas_trabalhadas():
    qtd_horas_trabalhadas = int(input("Quantas horas você trabalhou? "))
    return qtd_horas_trabalhadas

def calcula_hora_trabalhada(ganho_hora,horas_trabalhadas):
    resultado_ganho = ganho_hora * horas_trabalhadas

    return print("O resultado foi: R$",resultado_ganho)

ganho_reais = pergunta_ganho_hora()
qtd_horas = horas_trabalhadas()
calcula_hora_trabalhada(ganho_reais,qtd_horas)
    