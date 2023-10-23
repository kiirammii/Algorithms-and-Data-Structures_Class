number = int(input("número: "))
fatorial = 1 #por defeito, é 1

if number < 0:
    print ("inválido")
elif number == 0: #para o caso de ser 0
    print("o fatorial de 0 é 1")
else:
    for i in range (number, 1, -1): #vai desde o numero, até ao 1
        fatorial = fatorial * i #cálculo
    print("o fatorial de", number, "é", fatorial)