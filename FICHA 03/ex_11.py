quantidade = int(input("quantos números pretende inserir?: ")) # input para receber quantos números a verificar
maior = 0
segundo_maior = 0

if quantidade <= 0: # se for 0 ou menor
    print("inválida")
else:
    for i in range (quantidade): # repete as vezes pedidas pelo utilizador
        number = int(input("número: ")) 
        if number > maior: #se o numero for maior que o 'maior'
            segundo_maior = maior # o segundo maior passa a ter o valor do maior
            maior = number # o maior passa a ser o número lido

print(segundo_maior) # imprime