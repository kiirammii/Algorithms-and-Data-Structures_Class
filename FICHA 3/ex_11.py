quantidade = int(input("quantos números pretende inserir?: "))
maior = 0
segundo_maior = 0

if quantidade <= 0:
    print("inválida")
else:
    for i in range (quantidade):
        number = int(input("número: "))
        if number > maior:
            segundo_maior = maior
            maior = number

print(segundo_maior)