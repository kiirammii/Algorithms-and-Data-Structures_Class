def searchNumber(list, searchValue):
    
    positions = []
    
    for i in range (len(list)):
        if list[i] == searchValue:
            positions.append(i)
    
    return positions
        

list = []
for i in range (10):
    num = int(input("insira um número: "))
    list.append(num)

searchValue = int(input("\t\nnúmero a procurar: "))

result = searchNumber(list, searchValue)

if result:
    print("o número", searchValue, "aparece nas posições", result)
else:
    print("o número", searchValue, "não foi encontrado na lista.")