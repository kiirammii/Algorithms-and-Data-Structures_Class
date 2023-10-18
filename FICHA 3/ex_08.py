quantidade = int(input("quantos números na sequência?: "))
antepenultimo = 0
penultimo = 1
ultimoTermo = 0
sequencia = ''

if quantidade == 0:
    print("inválido")
elif quantidade == 1:
    print(antepenultimo)
elif quantidade == 2:
    print(penultimo)
else:
    sequencia += str(antepenultimo) + '  ' + str(penultimo)
    for i in range (3, quantidade+1):
        ultimoTermo = int(antepenultimo) + int(penultimo)
        sequencia += '  ' + str(ultimoTermo)
        antepenultimo = penultimo
        penultimo = ultimoTermo
    print (sequencia)
