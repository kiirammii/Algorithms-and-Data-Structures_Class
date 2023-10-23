def somatorio(num1, num2):
    soma = 0
    if num1 > num2:
        for i in range(num1, num2-1, -1):
            soma += i
    elif num2 > num1:
        for i in range(num2, num1-1, -1):
            soma += i

    return soma

num1 = int(input("1º número: "))
num2 = int(input("2º número: "))
print(somatorio(num1,num2))