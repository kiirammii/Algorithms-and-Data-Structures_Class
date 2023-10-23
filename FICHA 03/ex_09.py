number = int(input("numero: "))
total = 0 #total é 0 no inicio

if number <= 0: #se for menor que 0
    print("inválido")
elif number == 1: #se for 1
    print(number, 'não é um número perfeito')
else: #para qualquer outro númerp
    for i in range (1, number):
        if number % i == 0: #divide por todos os números até ele mesmo
            total += i #se for divisivel adiciona ao total
    
    if total == number: #se for igual ao total, é perfeito
        print(number, 'é um número perfeito')
    else:
        print(number, 'não é um número perfeito')