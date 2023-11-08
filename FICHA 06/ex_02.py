import random

answer = 'Y' # resposta para "começar denovo" é verdadeira por defeito

while answer == 'Y':
    def generateNumbers(lowerLimit, upperLimit, quant):
        key = []

        while len(key) != quant:
            num = random.randint(lowerLimit, upperLimit)
            if num not in key:
                key.append(num)
        
        return key
    
    print("Chave:", generateNumbers(1,50,5),"\tEstrelas:", generateNumbers(1,12,2))
    
    answer = str(input("gerar nova chave? (Y/N): ")) #pede para recomeçar
    if answer == 'N': #se for "N" fecha
        exit()
    else:
        print("\n-------------------\n")