def abundant(number):
    """esta função determina se um número é abundante ou não"""

    total = 0 #total é 0 no inicio

    if number <= 0: #se for menor que 0
        print("inválido")
    elif number == 1: #se for 1
        print(number, 'não é um número abundante')
    else: #para qualquer outro número
        for i in range (1, number):
            if number % i == 0: #divide por todos os números até ele mesmo
                total += i #se for divisivel adiciona ao total
        
        if total > number: #se for maior que o total, é abundante
            print(number, 'é um número abundante')
        else:
            print(number, 'não é um número abundante')


number = int(input("numero: ")) # recolhe o número
abundant(number) # imprime