quantidade = int(input("quantos números pretende inserir?: "))
segundo_maior = 0

if quantidade <= 0:
    print("inválida")
else:
    for i in range (1, quantidade+1):
        number = int(input("número: "))
        if number < maior and number > segundo_maior:
            segundo_maior = number

print(segundo_maior)