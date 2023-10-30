import random # biblioteca random

def generatePassword(username):
    """esta função gera uma password baseada num nome"""

    password = '' # password vazia
    nameLetters = '' # armazena as letras do nome
    
    space = username.find(' ') # procura o primeiro espaço, caso o nome seja composto
    if space != -1: # caso o nome seja composto, devolve inválido
        print('inválido')
    else:
        for i in range (1, len(username), 2): # começa a procura pela segunda letra, indo de 2 em 2
            nameLetters += username[i] # adiciona as letras à string

        for i in range (0, len(nameLetters)): # percorre a string com as letras do nome
            num = random.randint(1,9) # gera um numero aleatorio entre 1 e 9
            password = password + nameLetters[i] + str(num) # adiciona a letra da string e um numero aleatorio à password

        password = password + str(len(password)) # adiciona o numero de caracteres do nome no fim da password
        return password

nome = input("insira um nome: ") # recolhe o nome
print(generatePassword(nome)) # chama a função e imprime