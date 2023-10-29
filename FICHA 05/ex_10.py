import math

def printCharLine (text, num):
    number = len(text)/num
    ciclos = math.ceil(number)

    min = 0
    max = num

    for i in range (ciclos):
        subtext = text[min:max]
        min += num
        max += num
        
        print(subtext)

text = 'este e um texto para verificar o exercicio 10 da ficha 5 de AED'
num = 10
printCharLine(text, num)