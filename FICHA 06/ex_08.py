def removeDuplicates(list):
    list.sort()

    newList = []

    for number in list:
        if number not in newList:
            newList.append(number)

    return newList

listNumbers = []
quant = int(input('quantos números pretende inserir? '))
for i in range (quant):
    num = int(input('número: '))
    listNumbers.append(num)

print(removeDuplicates(listNumbers))