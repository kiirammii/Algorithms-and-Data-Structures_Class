def somatorio(num1, num2):
    """esta função calcula o somatório de 2 números"""

    soma = 0 # inicialmente, o somatorio é 0
    if num1 > num2: # se o primeiro numero for maior que o segundo
        for i in range(num2, num1): # o range é do segundo para o primeiro
            soma += i # adiciona i ao somatorio
    elif num2 > num1: # se o primeiro numero for manor que o segundo
        for i in range(num1, num2): # o range é do primeiro para o segundo
            soma += i # adiciona i ao somatorio

    return soma # devolve o somatorio

num1 = int(input("1º número: ")) # recolhe o 1º numero
num2 = int(input("2º número: ")) # recolhe o 2º numero
print(somatorio(num1,num2)) # imprime o somatorio