nome = input("Frase: ") # recolhe o nome

nomeInverso = '' # nome inverso, inicialmente, é uma string vazia
for i in range(len(nome)-1, -1, -1): # percorre todos os caracteres do nome, ao contrário
    nomeInverso += nome[i] # adiciona cada caractere à string

print(nomeInverso) # imprime

#alternativa
print(nome[::-1])