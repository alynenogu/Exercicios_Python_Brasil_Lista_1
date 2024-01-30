#Faça um Programa que peça um número e então mostre a mensagem 
#O número informado foi [número].


def pergunta_numero():
    resultado = int(input("Escolha um número: "))
    return resultado

#def mostre_numero(resultado):
#    print("O número informado foi: ", resultado)

def par_ou_impar(resultado):
    if resultado % 2 ==0:
        print("O número é par e foi: ",resultado)
    elif resultado % 2 != 0:
        print("O número é ímpar e foi: ",resultado)

par_ou_impar(pergunta_numero())