def standardName(nome):
    espaco1 = nome.find(' ')
    espaco2 = nome.rfind(' ')
    
    primeiroNome = nome[0:espaco1]
    ultimoNome = nome[espaco2+1:]

    nomeStandard = primeiroNome + ' '
    
    counter = nome.count(' ')
    posX = 0
    for i in range (1, counter):
        pos = nome.find(' ', posX)
        inicial = str(nome[pos+1]) + '. '
        nomeStandard += inicial
        posX = pos+1

    nomeStandard += ultimoNome
    return nomeStandard
    
nome = input('Insira um nome: ')
print(standardName(nome))