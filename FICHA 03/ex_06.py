import random #biblioteca random

answer = 'Y'

while answer == 'Y':
    ano = random.randint(1900, 2020) #escolhe um número entre 1900 e 2020

    if ano % 400 == 0: # se for divisivel por 400
        print (ano, "é um ano bissexto")
    if ano % 4 == 0 and ano % 100 != 0: # se for divisivel por 4 e não por 100
        print (ano, "é um ano bissexto")
    else: print (ano, "não é um ano bissexto") # caso as duas condições anteriores falhem

    answer = str(input("gerar novo ano? (Y/N): ")) # input que recolhe a resposta para recomeçar

    if answer == 'N': # se for não, sai
        exit()
    else: print ("\n-------------\n") # reinicia