def capicua(nome):
    """esta função determina se uma palavra é uma capicua ou não"""

    nomeMin = nome.lower() # converte para minusculas
    nomeInverso = '' # nome invertido é uma string vazia, inicialmente

    for i in range(len(nomeMin)-1, -1, -1): # percorre todos os caracteres do nome, do fim para o inicio
        nomeInverso += nomeMin[i] # escreve o nome ao contrario

    if nomeInverso == nomeMin: # se o inverso for igual ao nome
        return True # devolve True (capicua)
    else: return False # se não, devolve False

nome = input('insira uma frase: ') # recolhe o nome
capicua(nome) # chama a função, com o nome passado como parâmetro

if capicua(nome): # se for capicua, imprime que é
    print (nome, "é uma capicua")
else: print (nome, "não é uma capicua") # se não for capicua, imprime que não é