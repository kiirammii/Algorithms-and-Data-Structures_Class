number = int(input("numero: "))
total = 0

if number <= 0:
    print("inválido")
elif number == 1:
    print(number, 'não é um número perfeito')
else:
    for i in range (1, number):
        if number % i == 0:
            total += i
    
    if total == number:
        print(number, 'é um número perfeito')
    else:
        print(number, 'não é um número perfeito')