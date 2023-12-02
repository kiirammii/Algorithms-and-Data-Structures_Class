import random

def initMatriz():
    dim = int(input('\n\tDimensão da matriz: '))
    lista = []

    for i in range (dim):
        lista.append([])
        for j in range (dim):
            cell = random.randint(10,100)
            lista[i].append(cell)

    print('\nMatriz Gerada\n--------------')
    for i in range (dim):
        for j in range (dim):
            print(lista[i][j], end=" ")
        print()
    print()

def transMatriz():
    dim = int(input('\n\tDimensão da matriz: '))
    lista = []

    for i in range (dim):
        lista.append([])
        for j in range (dim):
            cell = random.randint(10,100)
            lista[i].append(cell)

    print('\nMatriz Gerada\n--------------')
    for i in range (dim):
        for j in range (dim):
            print(lista[i][j], end=" ")
        print()
    print()

    print('\nMatriz Transposta\n--------------')
    for i in range (dim):
        for j in range (dim):
            print(lista[j][i], end=" ")
        print()
    
def maiorMatriz():
    dim = int(input('\n\tDimensão da matriz: '))
    lista = []

    for i in range (dim):
        lista.append([])
        for j in range (dim):
            cell = random.randint(10,100)
            lista[i].append(cell)

    maior = 0
    for i in range (dim):
        for j in range (dim):
            if lista[j][i] >= 0:
                maior = lista[j][i]
    
    print('\n\tO maior valor da matriz é', lista[j][i])

# ---------------------

print('\tMENU\n1 - Inicializar Matriz\n2 - Matriz Transposta\n3 - Maior Valor\n0 - Sair')
option = int(input('\n\tEscolha uma Opção: '))

match option:
    case 1:
        initMatriz()
        
    case 2:
        transMatriz()

    case 3:
        maiorMatriz()

    case 4:
        print()