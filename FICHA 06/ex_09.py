diasSemana = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def numberOfVisitors(visitantes, dias):

    visitantesCopy = visitantes.copy() # 8 3 6 2

    visitantes.sort(reverse = True)
    visitantesOrder = visitantes # 8 6 3 2

    lista = []

    for visitante in visitantesOrder:
        result = ''
        pos = visitantesCopy.index(visitante)
        result += str(dias[pos]) + ' - ' + str(visitantesCopy[pos])
        lista.append(result)

    return '\n'.join(lista)

visitantes = []
for dia in diasSemana:
    valor = int(input('Visitors on {0}: '.format(dia)))
    visitantes.append(valor)

print('------------------')
print(numberOfVisitors(visitantes, diasSemana))

print('\n\t\tvisitors per day: ', format((sum(visitantes) / len(diasSemana)), '.2f'))