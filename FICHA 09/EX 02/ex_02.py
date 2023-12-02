'''
import random
from datetime import datetime
import time

def saveFile(linha):
    fTemp = open("FICHA 09/EX 02/temps.txt", "a")
    fTemp.write(linha)
    fTemp.close()

fim = False
while not fim:
    temp = random.randint(10,25)
    date = datetime.now().date()
    hour = datetime.now().time().strftime("%H:%M:%S")

    linha = str(date) + ";" + str(hour) + ";" + str(temp) + '\n'
    saveFile(linha)
    time.sleep(1)
'''

#----------------------------------------------------------------

print('\tMENU\n1 - Consulta por data\n2 - Consulta por estatistica')
option = int(input('\n\tEscolha uma Opção: '))

match option:
    case 1:
        dataSearch = input('\n\tInsira uma Data (ano-mes-dia): ')

        f = open("FICHA 09/EX 02/temps.txt", "r")
        linhas = f.readlines()
        f.close()

        print ('\n\n\t Data\t         Hora\t         Temperatura')
        print('\t---------------------------------------------')

        for linha in linhas:
            data, hora, temperatura = linha.strip().split(';')
            if dataSearch == data:
                print('\t', data, '\t', hora, '\t', temperatura)

    case 2:
        f = open("FICHA 09/EX 02/temps.txt", "r")
        linhas = f.readlines()
        f.close()

        temperaturas = []

        for linha in linhas:
            data, hora, temperatura = linha.strip().split(';')
            temperaturas.append(int(temperatura))

        temperaturas.sort()

        minTemp = temperaturas[0]
        maxTemp = temperaturas[-1]
        medTemp = float(sum(temperaturas)/len(temperaturas))

        print('\n\tA menor temperatura registada foi', minTemp)
        print('\tA maior temperatura registada foi', maxTemp)
        print('\tA media das temperaturas registadas foi', medTemp)

