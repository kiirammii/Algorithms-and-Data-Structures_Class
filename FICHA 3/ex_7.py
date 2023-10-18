number = int(input("numero: "))
isPrime = True

if number <= 1:
    print('inválido')
elif number == 2:
    print("o numero", number, "é primo")
else:
    for i in range (2, number):
        if number % i == 0:
            isPrime = False
            break
        else:
            break

    if isPrime:
        print ("o numero", number, "é primo")
    else: print ("o numero", number, "não é primo")