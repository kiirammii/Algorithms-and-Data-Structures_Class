number = int(input("numero: "))

if number <= 1:
    print('inválido')
else:
    for i in range (2, number):
        if number % i == 0:
            print ("o numero", number, "não é primo")
            break
        else:
            print("o numero", number, "é primo")
            break
    

#numero 2 não printa