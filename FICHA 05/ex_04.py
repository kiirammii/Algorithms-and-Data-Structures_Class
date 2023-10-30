def removeSpaces(frase):
    """esta função remove os espaços a mais de uma frase"""

    counter = frase.count(' ') # conta o número de espaços na frase

    for i in range (counter-1): # repete um ciclo n vezes equivalente à quantidade de espaços na frase
        frase = frase.replace('  ',' ') # substitui os espaços duplos na frase por um unico espaço

    print(frase) # imprime a frase sem os espaços a mais

frase = input('Insira uma frase: ') # recolhe a frase
removeSpaces(frase) # chama a função com a frase como parâmetro