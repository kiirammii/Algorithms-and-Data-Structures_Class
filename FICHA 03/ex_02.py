import math #biblioteca math

maior = -math.inf #menor número possivel
total = 0

numeros = int(input("quantos números quer inserir?: "))

for i in range(numeros): #repete quantas vezes o utilizador pedir
    number = float(input("número: "))
    total += number #adiciona o numero ao total
    if number > maior:
        maior = number #se o numero for maior que o "maior", passa a ser o maior

media = total / numeros
print ("a média total dos números é", media)
print ("o maior número é", maior)