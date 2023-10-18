import random #biblioteca random

answer = 'Y' # resposta para "começar denovo" é verdadeira por defeito

while answer == 'Y': #enquanto a resposta for "sim"

    numero = random.randint(1, 50) #escolhe um número entre 1 e 50
    palpite = int(input("indique o seu palpite: "))
    tentativas = 1 #minimo de 1 tentativa

    while palpite != numero: #enquanto não acertar
        if tentativas == 10: #se chegar as 10 tentativas
            print ("esgotou as 10 tentativas") 
            break
        
        if palpite > numero:
            print("\to número é menor. tente novamente\n") #resposta se for maior que o número
        if palpite < numero:
            print("\to número é maior. tente novamente\n") #resposta se for menor que o número

        tentativas += 1 #adiciona mais uma tentativa ao contador
        palpite = int(input("indique o seu palpite: "))


    #quando o palpite for certo, para o ciclo while e printa "correto" e o numero de tentativas
    if tentativas != 10:
        print ("\tcorreto :)\n\tacertou em", tentativas, "tentativas")
    answer = str(input("novo jogo? (Y/N): ")) #pede para recomeçar

    if answer == 'N': #se for "N" fecha
        exit()
    else:
        print("\n-------------------\n")