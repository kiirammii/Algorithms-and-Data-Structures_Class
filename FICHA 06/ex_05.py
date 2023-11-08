meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def highestSales(meses, valores):
    maior = max(valores)
    maiorMes = meses[valores.index(maior)]

    return maiorMes

def lowestSales(meses, valores):
    maior = min(valores)
    maiorMes = meses[valores.index(maior)]

    return maiorMes

def averageSales(meses, valores):
    media = sum(valores) / len(meses)

    return media


valores = []
for mes in meses:
    valor = int(input('Faturação no mês de {0}: '.format(mes)))
    valores.append(valor)

print()
print("\tmês de maior faturação: ", highestSales(meses, valores))
print("\tmês de menor faturação: ", lowestSales(meses, valores))
print("\tnúmero médio de faturação", averageSales(meses, valores))
print()