#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
#em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros
#quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 
#ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem
#compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor.
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
#considere latas cheias.

def pergunta_metros():
    metros = int(input("O valor em metros quadrados da área que deverá ser pintado :"))

    return metros

def calcula_cobertura_tinta(metros):
    cobertura = metros/6
    return round(cobertura,0)

def calcula_latas_tinta_18(cobertura):
    resultado_latas_18 = (cobertura/18)*1.1

    return round(resultado_latas_18,0)

def calcula_latas_tinta_3(cobertura):
    resultado_latas_3 = cobertura/3.6

    return round(resultado_latas_3,0)

def calcula_gasto_latas_18(resultado_latas_18):
    valor_gasto_18 = resultado_latas_18 * 80
    
    return valor_gasto_18

def calcula_gasto_latas_3(resultado_latas_3):
    valor_gasto_3 = resultado_latas_3 * 80
    
    return valor_gasto_3

qtd_metros = pergunta_metros()
valor_cobertura_tinta = calcula_cobertura_tinta(qtd_metros)
valor_qtd_tintas_18 = calcula_latas_tinta_18(valor_cobertura_tinta)
valor_qtd_tintas_3 = calcula_latas_tinta_3(valor_cobertura_tinta)
valor_gasto_latas_18 = calcula_gasto_latas_18(valor_qtd_tintas_18)
valor_gasto_latas_3 = calcula_gasto_latas_3(valor_qtd_tintas_3)
print("Cobertura que será pintada: ", valor_cobertura_tinta)
print("Quantidade de Latas que devem ser compradas, no caso de 18 litros: ", valor_qtd_tintas_18)
print("Quantidade de Latas que devem ser compradas, no caso de 3.6 litros: ", valor_qtd_tintas_3)
print("Valor Gasto com Latas de tintas, no caso de 18 litros: R$", valor_gasto_latas_18)
print("Valor Gasto com Latas de tintas, no caso de 3.6 litros: R$", valor_gasto_latas_3)