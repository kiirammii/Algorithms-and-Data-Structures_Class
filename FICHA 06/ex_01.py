def aboveAverage(numbers):

    media = sum(numbers) / len(numbers)
    count = 0

    for number in numbers:
        if number > media:
            count += 1

    return count

numbers = []
for i in range (10):
    num = int(input("número: "))
    numbers.append(num)
print(aboveAverage(numbers), "números estão acima da média")