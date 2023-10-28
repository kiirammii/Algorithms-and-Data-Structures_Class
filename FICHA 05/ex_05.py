def shortName(nome):
    espaco1 = nome.find(' ')
    espaco2 = nome.rfind(' ')

    primeiroNome = nome[0:espaco1]
    ultimoNome = nome[espaco2:]
    nomeCurto = primeiroNome + ultimoNome

    return nomeCurto
    
nome = input('Insira um nome: ')
print(shortName(nome))