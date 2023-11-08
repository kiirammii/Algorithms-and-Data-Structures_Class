def convertText(text):

    #substituição de todos os números
    text = text.replace('1', 'um ')
    text = text.replace('2', 'dois ')
    text = text.replace('3', 'tres ')
    text = text.replace('4', 'quatro ')
    text = text.replace('5', 'cinco ')
    text = text.replace('6', 'seis ')
    text = text.replace('7', 'sete ')
    text = text.replace('8', 'oito ')
    text = text.replace('9', 'nove ')

    counter = text.count(' ') # conta o número de espaços na frase

    for i in range (counter-1): # repete um ciclo n vezes equivalente à quantidade de espaços na frase
        text = text.replace('  ',' ') # substitui os espaços duplos na frase por um unico espaço

    return text

#recebe e imprime
text = str(input("insira um texto: "))
print(convertText(text))