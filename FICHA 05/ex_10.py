import math

def printCharLine (text, num):
    """esta função imprime n numero de caracteres de um texto por linha"""

    # determina quantos ciclos terá de fazer (linhas)
    number = len(text)/num # divide o numero de caracteres, pelo numero de caracteres por linha pedidos
    ciclos = math.ceil(number) # arredonda o valor para cima

    min = 0 # começa no 0
    max = num # acaba no numero pedido

    for i in range (ciclos): # repete o ciclo para todas as linhas do texto
        line = text[min:max] # primeira linha vai desde o valor minimo até ao valor n pedido
        min += num # adiciona num ao valor minimo
        max += num # adiciona num ao valor maximo
        
        print(line) # imprime a linha

text = 'este e um texto para verificar o exercicio 10 da ficha 5 de AED'
num = 10 # numero de caracteres por linha
printCharLine(text, num) # chama a função