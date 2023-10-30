frase = input('Insira uma frase: ') # recolhe a frase

fraseMin = frase.lower() # coloca tudo em minúsculas

numChars = len(fraseMin) # calcula o número de caracteres
numSpace = fraseMin.count(' ') # calcula o número de espaços
numVowels = fraseMin.count('a') + fraseMin.count('e') + fraseMin.count('i') + fraseMin.count('o') + fraseMin.count('u') # conta todas as vogais

#imprime 
print('nº de caracteres na frase: ', numChars)
print('nº de espaços na frase: ', numSpace)
print('nº de vogais na frase: ', numVowels)