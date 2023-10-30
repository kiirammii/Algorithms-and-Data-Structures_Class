def shortName(nome):
    """esta função, dado um nome completo, escreve apenas o primeiro e ultimo nome"""

    espaco1 = nome.find(' ') # procura o primeiro espaço
    espaco2 = nome.rfind(' ') # procura o ultimo espaço

    primeiroNome = nome[0:espaco1] # primeiro nome é desde o inicio até ao primeiro espaço (exclusive)
    ultimoNome = nome[espaco2:] # ultima nome é desde o ultimo espaço até ao fim (inclusive)
    nomeCurto = primeiroNome + ultimoNome # coloca ambos os nomes na string

    return nomeCurto # devolve o nome curto
    
nome = input('Insira um nome: ') # recolhe o nome completo
print(shortName(nome)) # chama a função e imprime 