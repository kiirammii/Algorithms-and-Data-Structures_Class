import math

maior = -math.inf #menor número possivel
total = 0

for i in range(10): #repete 10 vezes
    number = float(input("número: ")) #pede o número
    total += number #adiciona esse número ao total
    if number > maior: #se for número for o maior
        maior = number #passa a ser o maior

media = total / 10 #calcula a média
print ("a média total dos números é", media) 
print ("o maior número é", maior)