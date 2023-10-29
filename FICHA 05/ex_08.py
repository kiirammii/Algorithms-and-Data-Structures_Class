def reverseWords(text):
    reversedText = '' #armazena as palavras ao contrário
    word = '' #construir cada palavra ao contrário
    wordStarted = False #indica se a palavra está a ser contruida

    for char in text:
        if char != ' ':
            word += char
            wordStarted = True
        elif wordStarted:
            reversedText = word + ' ' + reversedText
            word = ""
            wordStarted = False

    if wordStarted:
        reversedText = word + ' ' + reversedText

    return reversedText

text = "This is an AED test"
print(reverseWords(text))