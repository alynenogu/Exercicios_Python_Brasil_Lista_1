#3.Faça um Programa que peça dois números e imprima a soma.

def informe_primeiro_numero():
    primeiro_numero = int(input("Digite o primeiro número: "))
    return primeiro_numero

def informe_segundo_numero():
    segundo_numero = int(input("Digite o segundo número: "))
    return segundo_numero

def soma_numeros(primeiro_numero,segundo_numero):
    soma = primeiro_numero + segundo_numero
    return print("Soma os dois números: ", soma)


soma_numeros(informe_primeiro_numero(),informe_segundo_numero())