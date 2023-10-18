number = int(input("número: "))

binario = ''

if number == 1:
    binario = '1'
else:
    while number > 0:
        resto = number % 2
        binario = str(resto) + binario
        number = number // 2

print(binario)