def calculteAverage(*numeros):
    """esta função calcula a média de um conjunto de números"""

    if len(numeros) == 0: # se não houverem números inseridos
        return 0 # devolve 0
    
    else:
        total = 0 # total inicialmente é 0
        for num in numeros: # para cada número no conjunto de números
            total += num # soma cada um ao total
        
        average = total / len(numeros) # divide o total pelo número de números (média)
        return average # devolve 

#recolha e impressão
average1 = calculteAverage(2,3,4)
average2 = calculteAverage(2,8,10,6,14)
print("Average 1:", average1)
print("Average 2:", average2)