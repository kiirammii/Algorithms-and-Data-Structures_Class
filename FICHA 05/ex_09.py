def countWord(text, word):
    quantity = 0
    counter = text.count('vehicle')
    posX = 0

    for i in range (1, counter):
        pos = text.find('vehicle', posX)
        quantity += 1
        posX = pos+1

    print(counter)
    return quantity

text = 'Using a GPS/GPRS unit installed in each vehicle, a monitoring device  records real-time  information about the location of  each vehicle'
print(countWord(text, 'vehicle'))