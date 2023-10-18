number = int(input("número: "))

binario = '' #string vazia

if number == 1: #se for 1, o binário é 1
    binario = '1'
else:
    while number > 0: #enquanto a divisão for possivel
        resto = number % 2 #o resto da divisão do número por 2
        binario = str(resto) + binario #adiciona atras na string o resto
        number = number // 2 #parte inteira da divisão do numero por 2

print(binario)