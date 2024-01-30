#Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
#trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o 
#sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
 
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido
 
def pergunta_qtd_hora():
    qtd_horas = int(input("Quatidade de horas trabalhadas por mês"))
    return qtd_horas

def pergunta_valor_hora():
    valor_hora = int(input("Qual é o valor hora"))
    return valor_hora

def calcula_salario_bruto(qtd_horas,valor_hora):
    salario_bruto = qtd_horas*valor_hora

    return salario_bruto

def calcula_inss (salario_bruto):
    valor_inss = (salario_bruto*8)/100
    return valor_inss

def calcula_sindicato (salario_bruto):
    valor_sindicato = (salario_bruto*5)/100
    return valor_sindicato

def calcula_imposto_renda (salario_bruto):
    valor_imposto_renda = (salario_bruto*11)/100
    return valor_imposto_renda
 
def calcula_salario_liquido (salario_bruto,valor_inss,valor_sindicato,valor_imposto_renda):
    salario_liquido = salario_bruto - valor_inss - valor_sindicato - valor_imposto_renda
    return salario_liquido

qtd_horas = pergunta_qtd_hora()
valor_hora = pergunta_valor_hora()
valor_salario_bruto = calcula_salario_bruto(qtd_horas,valor_hora)
valor_resultado_inss = calcula_inss(valor_salario_bruto)
valor_resultado_sindicato = calcula_inss(valor_salario_bruto)
valor_resultado_imposto_renda = calcula_imposto_renda(valor_salario_bruto)
valor_salario_liquido = calcula_salario_liquido(valor_salario_bruto, valor_resultado_inss,valor_resultado_sindicato,valor_resultado_imposto_renda)


print("+ Salário Bruto : R$",valor_salario_bruto)
print("- IR (11%) : R$",valor_resultado_imposto_renda)
print("- INSS (8%) : R$",valor_resultado_inss)
print("- Sindicato ( 5%) : R$",valor_resultado_sindicato)
print("= Salário Liquido : R$",valor_salario_liquido)



