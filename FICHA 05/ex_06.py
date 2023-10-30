def standardName(nome):
    """esta função recebe um nome completo e substitui os nomes do meio pela sua inicial"""

    espaco1 = nome.find(' ') # procura o primeiro espaço
    espaco2 = nome.rfind(' ') # procura o ultimo espaço
    
    primeiroNome = nome[0:espaco1] # primeiro nome é desde o inicio até ao primeiro espaço (exclusive)
    ultimoNome = nome[espaco2+1:] # ultima nome é desde o ultimo espaço até ao fim (inclusive) (+1 para não ter espaços adicionais)

    nomeStandard = primeiroNome + ' ' # começa a escrever o nome, começando por escrever o primeiro nome e um espaço
    
    counter = nome.count(' ') # conta o numero de espaços que tem
    pos = 0 # posição inicial é 0
    for i in range (1, counter): # repete um ciclo n vezes equivalente à quantidade de espaços na frase
        pos = nome.find(' ', pos) # procura o primeiro espaço desde a posição 0
        inicial = str(nome[pos+1]) + '. ' # inicial é igual à primeira letra apos o espaço mais um ponto
        nomeStandard += inicial # adiciona a inicial ao nome
        pos += 1 # avança para a posição seguinte

    nomeStandard += ultimoNome # adiciona o ultimo nome à string
    return nomeStandard # devolve
    
nome = input('Insira um nome: ') # recolhe o nome completo
print(standardName(nome)) # imprime