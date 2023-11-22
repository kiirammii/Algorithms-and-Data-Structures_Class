print('\tMENU\n1 - Inserir Países\n2 - Consulta Países\n3 - Consulta por Continente\n4 - Consulta nº Paises\n0 - Sair')
option = int(input('\n\tEscolha uma Opção: '))

def nPaisesCont():
    try:
        f = open("FICHA 09/EX 01/paises.txt", "r")
        linhas = f.readlines()
        f.close()

        continentes = []
        contagens = []

        for linha in linhas:
            pais, cont = linha.strip().split(';')

            if cont in continentes:
                indice = continentes.index(cont)
                contagens[indice] += 1
            else:
                continentes.append(cont)
                contagens.append(1)

        for i in range(len(continentes)):
            print(f'\t{continentes[i]}: {contagens[i]} países')
    except FileNotFoundError:
        print("Arquivo não encontrado.")

match option:
    case 0:
        print()
    
    case 1:
        pais = input('\n\t\tPaís: ')
        continente = input('\n\t\tContinente: ')
        line = pais + ';' + continente

        f = open("FICHA 09/EX 01/paises.txt", "r")
        linhas = f.readlines()
        f.close()

        linhaExiste = False

        for linha in linhas:
            if line == linha.strip():
                print('\n\tO país já existe na lista')
                linhaExiste = True
                break

        if linhaExiste == False:
            f = open("FICHA 09/EX 01/paises.txt", "a")
            line = line + '\n'
            f.write(line)
            f.close()
            print('\n\tPaís adicionado com sucesso !')
    
    case 2:
        f = open("FICHA 09/EX 01/paises.txt", "r")
        linhas = f.readlines()
        f.close()

        for linha in linhas:
            print(linha)

    case 3:
        continente = input('\n\t\tIndique um continente: ')

        f = open("FICHA 09/EX 01/paises.txt", "r")
        linhas = f.readlines()
        f.close()

        continentes = []

        for linha in linhas:
            pais, cont = linha.strip().split(';')
            if cont == continente:
                continentes.append(pais)

        if continentes:
            print('\n\tPaíses no continente', continente,)
            for pais in continentes:
                print('\t', pais)
        else:
            print('\n\tNão há países no continente', continente)

    case 4:
        nPaisesCont()