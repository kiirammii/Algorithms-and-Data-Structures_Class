diasSemana = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def numberOfVisitors(visitantes, dias):

    visitantesCopy = visitantes.copy()

    visitantes.sort(reverse = True)
    visitantesOrder = visitantes

    diasOrdenados = []
    for visitante in visitantesOrder:
        result = ''
        pos = visitantesCopy.index(visitante)
        result += str(dias[pos]) + ' - ' + str(visitantesCopy[pos])
        diasOrdenados.append(result)

    mediaValue = format((sum(visitantes) / len(dias)), '.2f')
    media = '\n\n\n\t\tAverage Number of Visitors per Day: ' + mediaValue

    numMaisProximo = min(visitantesCopy, key=lambda x: abs(x - float(mediaValue)))
    indexMaisProximo = visitantesCopy.index(numMaisProximo)
    diaMaisProximo = '\n\t\tClosest to Average: ' + str(dias[indexMaisProximo])

    result = '\n\t' + '\n\t'.join(diasOrdenados) + media + diaMaisProximo

    return result

visitantes = []
for dia in diasSemana:
    valor = int(input('Visitors on {0}: '.format(dia)))
    visitantes.append(valor)

print('------------------')
print(numberOfVisitors(visitantes, diasSemana))