import random

def generatePassword(username):
    password = ''
    nameVowels = ''
    
    space = username.find(' ')
    if space != -1:
        print('inválido')
    else:
        for i in range (1, len(username), 2):
            nameVowels += username[i]

        for i in range (0, len(nameVowels)):
            num = random.randint(1,9)
            password = password + nameVowels[i] + str(num)

        password = password + str(len(password))
        return password

nome = input("insira um nome: ")
print(generatePassword(nome))