import math

maior = -math.inf
total = 0

for i in range(10):
    number = float(input("número: "))
    total += number
    if number > maior:
        maior = number

media = total / 10
print ("a média total dos números é", media)
print ("o maior número é", maior)