

def fibonacci(quantidade):
    antepenultimo = 0 #primeiro valor é 0
    penultimo = 1 #segundo é 1
    ultimoTermo = 0 #terceiro termo é 0, por enquanto
    sequencia = '' #sequencia vazia

    if quantidade == 0: #se for 0
        print("inválido")
    elif quantidade == 1: #se for 1
        print(antepenultimo)
    elif quantidade == 2: #se for 2
        print(penultimo)
    else: #se for 3 ou mais
        sequencia += str(antepenultimo) + '  ' + str(penultimo) #sequencia incial é 0, 1
        for i in range (3, quantidade+1): #do 3 até ao numero querido
            ultimoTermo = antepenultimo + penultimo #o termo é a soma dos dois anteriores
            sequencia += '  ' + str(ultimoTermo) #adiciona o termo calculado à sequencia
            antepenultimo = penultimo #o valor do terceiro ultimo termo passa a ser o valor do segundo ultimo
            penultimo = ultimoTermo #o valor do segundo ultimo termo passa a ser o valor do ultimo
        print (sequencia)
        
quantidade = int(input("quantos números na sequência?: "))
fibonacci(quantidade)