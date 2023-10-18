import math

maior = -math.inf
total = 0

numeros = int(input("quantos números quer inserir?: "))

for i in range(numeros):
    number = float(input("número: "))
    total += number
    if number > maior:
        maior = number

media = total / numeros
print ("a média total dos números é", media)
print ("o maior número é", maior)