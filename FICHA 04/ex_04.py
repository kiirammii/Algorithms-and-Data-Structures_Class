def calculteAverage(*numeros):
    if len(numeros) == 0:
        return 0
    
    else:
        total = 0
        for num in numeros:
            total += num
        
        average = total / len(numeros)
        return average

average1 = calculteAverage(2,3,4)
average2 = calculteAverage(2,8,10,6,14)
print("Average 1:", average1)
print("Average 2:", average2)