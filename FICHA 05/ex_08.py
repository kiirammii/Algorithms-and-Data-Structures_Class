def reverseWords(text):
    reversedText = ''

    posX = 0
    counter = text.count(' ')

    for i in range (1, counter):
        pos = text.rfind(' ', posX)
        reversedText = reversedText + text[pos:]
        text = text[0:pos-1]
        posX = pos+1

    return reversedText

text = input('insira um texto: ')
print(reverseWords(text))