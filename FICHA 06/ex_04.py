def positiveList(numbers, names):
    positiveScores = []
    positiveNames = []

    for num in numbers:
        if num >= 10:
            pos = numbers.index(num)
            positiveScores.append(num)
            positiveNames.append(names[pos])

    return positiveScores, positiveNames

try:
    numbers = []
    names = []
    for i in range (3):
        name = str(input("Nome: "))
        num = int(input("pontuação (0 - 20): "))
        print("-----")
        if 0 <= num <= 20:
            numbers.append(num)
            names.append(name)
        else: raise ValueError
except:
    print("valor incorreto")

print("pontuações positivas:", positiveList(numbers, names))