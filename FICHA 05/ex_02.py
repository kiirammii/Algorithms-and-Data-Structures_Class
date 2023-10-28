frase = input('Insira uma frase: ')

fraseMin = frase.lower()

numChars = len(fraseMin)
numSpace = fraseMin.count(' ')
numVowels = fraseMin.count('a') + fraseMin.count('e') + fraseMin.count('i') + fraseMin.count('o') + fraseMin.count('u')

print('nº de caracteres na frase: ', numChars)
print('nº de espaços na frase: ', numSpace)
print('nº de vogais na frase: ', numVowels)