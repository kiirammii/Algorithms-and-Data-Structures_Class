nome = input("Frase: ")

nomeInverso = ''
for i in range(len(nome)-1, -1, -1):
    nomeInverso += nome[i]

print(nomeInverso)

#alternativa
print(nome[::-1])