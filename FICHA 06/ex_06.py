def searchNumber(list, searchValue):
    
    positions = []
    pos = 0
    
    for i in range (len(list)):
        pos = list.index(searchNumber, pos)
        positions.append(pos)
        pos += 1
        
    return positions
        

list = []
for i in range (5):
    num = int(input("insira um número: "))
    list.append(num)

searchValue = int(input("\t\nnúmero a procurar: "))

result = searchNumber(list, searchValue)

if result:
    print("o número", searchValue, "aparece nas posições", result)
else:
    print("o número", searchValue, "não foi encontrado na lista.")