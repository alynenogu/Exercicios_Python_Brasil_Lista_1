#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

def pergunta_numeros_inteiros(mensagem):
    numero = int(input(mensagem))
    

    return numero

#def pergunta_numeros_inteiros_segundo():
   
#    segundo_numero = int(input("Digite o segundo número inteiro: "))

 #   return segundo_numero

def pergunta_numero_real():
    terceiro_numero = float(input("Digite o terceiro número decimal: "))

    return terceiro_numero

def calcula_dobro_primeiro_segundo(primeiro_numero,segundo_numero):
    resultado_primeiro_segundo = ((primeiro_numero)*2) + (segundo_numero/2)
    return resultado_primeiro_segundo

def calcula_primeiro_terceiro (primeiro_numero,terceiro_numero):
    resultado_primeiro_terceiro = (primeiro_numero*3)+terceiro_numero
    return resultado_primeiro_terceiro

def calcula_terceiro_cubo(terceiro_numero):
    resultado_terceiro_cubo = terceiro_numero**3
    return  resultado_terceiro_cubo

primeiro_valor = pergunta_numeros_inteiros("Digite o primeiro número: ")
segundo_valor = pergunta_numeros_inteiros("Digite o segundo número: ")
terceiro_valor = pergunta_numero_real()
resultado_dobro_primeiro_segundo = calcula_dobro_primeiro_segundo(primeiro_valor,segundo_valor)
resultado_dobro_primeiro_terceiro = calcula_primeiro_terceiro(primeiro_valor,terceiro_valor)
resultado_terceiro_cubo = calcula_terceiro_cubo(terceiro_valor)

print("O produto do dobro do primeiro com metade do segundo é: ", resultado_dobro_primeiro_segundo)
print("a soma do triplo do primeiro com o terceiro", resultado_dobro_primeiro_terceiro)
print("O terceiro elevado ao cubo:",resultado_terceiro_cubo)

