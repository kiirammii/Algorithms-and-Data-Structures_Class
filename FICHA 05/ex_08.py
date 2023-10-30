def reverseWords(text):
    """esta função reescreve um texto com as palavras na ordem inversa"""

    reversedText = '' # string vazia

    for i in range (text.count(' ')+1): # ciclo repete tantas quanto espaços existentes
        pos = text.rfind(' ') # a partir do fim, procura o primeiro espaço
        word = text[pos+1:] # a primeira palavra do texto invertido vai ser desde o ultimo espaço até ao fim
        reversedText += word + ' ' # adiciona à string, junto de um espaço
        text = text[:pos] # exclui a ultima palavra do texto e volta a procurar

    return reversedText # devolve o texto invertido

text = "This is an AED test"
print(reverseWords(text)) # chama a função e imprime