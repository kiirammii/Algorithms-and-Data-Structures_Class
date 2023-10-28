def capicua(nome):

    nomeMin = nome.lower()
    nomeInverso = ''
    for i in range(len(nomeMin)-1, -1, -1):
        nomeInverso += nomeMin[i]

    if nomeInverso == nomeMin:
        return True
    else: return False

nome = input('insira uma frase: ')
capicua(nome)

if capicua(nome):
    print (nome, "é uma capicua")
else: print (nome, "não é uma capicua")