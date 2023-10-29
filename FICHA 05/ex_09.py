def countWord(text, word):
    occurrences = 'Posições: '
    count = 0
    start = 0

    while True:
        index = text.find(word, start)

        if index == -1:
            break

        if count > 0:
            occurrences += ", "

        occurrences += str(index)
        count += 1
        start = index + 1

    return count , occurrences

text = "Using a GPS/GPRS unit installed in each vehicle, a monitoring device records real-time information about the location of each vehicle."
word = 'vehicle'
print(countWord(text, word))