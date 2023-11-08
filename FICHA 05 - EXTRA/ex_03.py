def countRepeat(text):
    text = text.lower()

    words = text.split(' ')

    uniqueWords = []
    repeatedWords = []

    for word in words:
        if word in uniqueWords and word not in repeatedWords:
            repeatedWords.append(word)
        else:
            uniqueWords.append(word)

    return repeatedWords

text = 'Exercicio de AED parecido com o exercicio do teste de AED'
print(countRepeat(text))