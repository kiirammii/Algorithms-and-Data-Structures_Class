def positiveList(numbers):
    positiveScores = []

    for num in numbers:
        if num >= 10:
            positiveScores.append(num)

    return positiveScores


try:
    numbers = []
    for i in range (10):
        num = int(input("pontuação (0 - 20): "))
        if 0 <= num <= 20:
            numbers.append(num)
        else: raise ValueError
except:
    print("valor incorreto")

print("pontuações positivas:", positiveList(numbers))