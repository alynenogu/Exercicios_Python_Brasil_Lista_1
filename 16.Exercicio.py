#Faça um programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
#tinta é vendida em latas de 18 litros, que custam R$ 80,00.
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

def pergunta_metros():
    metros = int(input("O valor em metros quadrados da área que deverá ser pintado :"))

    return metros

def calcula_cobertura_tinta(metros):
    cobertura = metros/3
    return cobertura

def calcula_latas_tinta(cobertura):
    resultado_latas = cobertura/18

    return resultado_latas

def calcula_gasto_latas(resultado_latas):
    valor_gasto = resultado_latas * 80
    
    return valor_gasto

qtd_metros = pergunta_metros()
valor_cobertura_tinta = calcula_cobertura_tinta(qtd_metros)
valor_qtd_tintas = calcula_latas_tinta(valor_cobertura_tinta)
valor_gasto_latas = calcula_gasto_latas(valor_qtd_tintas)
print("Cobertura que será pintada: ", valor_cobertura_tinta)
print("Quantidade de Latas que devem ser compradas: ", valor_qtd_tintas)
print("Valor Gasto com Latas de tintas: R$", valor_gasto_latas)
