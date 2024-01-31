#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de 
#um link de Internet (em Mbps), 
#calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

def pergunta_tamanho_arquivo():
    tamanho_arquivo = int(input("Qual é o tamanho do arquivo em MB?"))

    return tamanho_arquivo

def pergunta_velocidade_internet():
    velocidade_internet = int(input("Qual é a velocidade da sua internet?"))

    return velocidade_internet

def calcula_tempo (tamanho_arquivo,velocidade_internet):

    tempo = tamanho_arquivo/velocidade_internet
    tempo_em_minutos = tempo/60

    return tempo_em_minutos

resposta_tamanho_arquivo = pergunta_tamanho_arquivo()
resposta_velocidade = pergunta_velocidade_internet()
resposta_calcula_tempo = calcula_tempo(resposta_tamanho_arquivo,resposta_velocidade)
print("O tempo aproximado em minutos é: ",resposta_calcula_tempo)