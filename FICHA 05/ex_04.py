def removeSpaces(frase):
    counter = frase.count(' ')

    for i in range (counter):
        frase = frase.replace('  ',' ')

    print(frase)

frase = input('Insira uma frase: ')
removeSpaces(frase)