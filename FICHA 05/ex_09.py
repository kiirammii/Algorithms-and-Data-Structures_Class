def countWord(text, word):
    occurrences = 'Posições: '
    count = 0 # contagem de vezes que a palavra aparece
    pos = 0 # posição inicial de onde começa a contar

    while True:
        index = text.find(word, pos) # procura o index da palavra, desde o 0

        if index == -1: # se não existir, quebra
            break

        if count > 0: # adiciona uma virgula se ja existir algo na string 
            occurrences += ", "

        occurrences += str(index) # adiciona a posição da palavra na string
        count += 1 
        pos = index + 1 # volta a procurar desde a ultima palavra

    return count , occurrences

text = "Using a GPS/GPRS unit installed in each vehicle, a monitoring device records real-time information about the location of each vehicle."
word = 'vehicle'
print(countWord(text, word))