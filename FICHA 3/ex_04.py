import random #biblioteca random

numero = random.randint(1, 50) #escolhe aleatoriamente um número entre 1 e 50
palpite = int(input("indique o seu palpite: "))
tentativas = 1 #o utilizador utiliza sempre 1 tentativa

while palpite != numero: #se o palpite for diferente do número
    if tentativas == 10: #se chegar as 10 tentativas
        print ("esgotou as 10 tentativas")
        exit() #fecha o programa

    if palpite > numero: #se for maior
        print("\to número é menor. tente novamente\n")
    if palpite < numero: #se for menor
        print("\to número é maior. tente novamente\n")
    tentativas += 1 #adiciona uma tentativa ao contador
    palpite = int(input("indique o seu palpite: "))
    
#quando o palpite for certo, para o ciclo while e printa "correto" e o numero de tentativas
print ("\tcorreto :)\n\tacertou em", tentativas, "tentativas") 