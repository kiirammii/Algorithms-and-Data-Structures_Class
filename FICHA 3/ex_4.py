import random

numero = random.randint(1, 50)
palpite = int(input("indique o seu palpite: "))
tentativas = 1

while palpite != numero:
    if tentativas == 10:
        print ("esgotou as 10 tentativas")
        exit()

    if palpite > numero:
        print("\to número é menor. tente novamente\n")
    if palpite < numero:
        print("\to número é maior. tente novamente\n")
    tentativas += 1
    palpite = int(input("indique o seu palpite: "))

    

#quando o palpite for certo, para o ciclo while e printa "correto" e o numero de tentativas
print ("\tcorreto :)\n\tacertou em", tentativas, "tentativas") 