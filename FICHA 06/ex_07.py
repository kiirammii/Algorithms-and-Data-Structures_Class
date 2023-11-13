meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def rainfall(rainfallList, meses):

    rainfallCopy = rainfallList.copy() # 8 3 6 2

    rainfallList.sort(reverse = True)
    rainfallOrder = rainfallList # 8 6 3 2

    lista = []

    for pluv in rainfallOrder:
        result = ''
        pos = rainfallCopy.index(pluv)
        result += str(meses[pos]) + ' - ' + str(rainfallCopy[pos])
        lista.append(result)

    return '\n'.join(lista)

rainfallList = []
for mes in meses:
    valor = int(input('Pluviosidade no mês de {0}: '.format(mes)))
    rainfallList.append(valor)

print('------------------')
print(rainfall(rainfallList, meses))