def removeSpaces(frase):
    frase = frase.replace('  ',' ', -1)
    print(frase)

frase = input('Insira uma frase: ')
removeSpaces(frase)