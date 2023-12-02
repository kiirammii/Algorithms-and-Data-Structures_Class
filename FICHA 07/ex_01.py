lista = []

for i in range (3):
    lista.append([])
    for j in range (3):
        cell = int(input('linha {0}, coluna {1}:' .format(i+1, j+1)))
        lista[i].append(cell)

for i in range (3):
    for j in range (3):
        print(lista[j][i], end=" ")
    print()