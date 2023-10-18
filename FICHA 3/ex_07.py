number = int(input("numero: "))
isPrime = True #é primo por defeito

if number <= 1: #se for menor ou igual a 1
    print('inválido')
elif number == 2: #se for 2
    print("o numero", number, "é primo")
else:
    for i in range (2, number): #para qualquer outro numero
        if number % i == 0: #se for divisivel por qualquer outro numero que não 1 ele mesmo
            isPrime = False #é falso ^
            break
        else:
            break

    if isPrime: #se for verdadeiro (oculto)
        print ("o numero", number, "é primo")
    else: print ("o numero", number, "não é primo")