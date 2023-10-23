import random #biblioteca random

answer = 'Y'

while answer == 'Y':
    ano = random.randint(1900, 2020) #escolhe um número entre 1900 e 2020

    if ano % 400 == 0:
        print (ano, "é um ano bissexto")
    if ano % 4 == 0 and ano % 100 != 0:
        print (ano, "é um ano bissexto")
    else: print (ano, "não é um ano bissexto")

    answer = str(input("gerar novo ano? (Y/N): "))

    if answer == 'N':
        exit()
    else: print ("\n-------------\n")