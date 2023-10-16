number = int(input("número: "))

binario = ''

while number / 2 != 0:
    resultado = number / 2
    resto = number % 2
    binario += str(resto)
    number = resultado

print(binario)