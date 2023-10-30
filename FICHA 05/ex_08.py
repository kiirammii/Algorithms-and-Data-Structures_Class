def reverseWords(text):
    reversedText = ''

    for i in range (text.count(' ')+1):
        pos = text.rfind(' ')
        word = text[pos+1:]
        reversedText += word + ' '
        text = text[:pos]

    return reversedText

text = "This is an AED test"
print(reverseWords(text))