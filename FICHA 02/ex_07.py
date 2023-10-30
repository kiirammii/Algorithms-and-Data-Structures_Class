print("Planet Codes\n\t1 - Mercury\n\t2 - Venus\n\t3 - Mars\n\t4 - Jupiter\n\t5 - Saturn\n\t6 - Uranus\n\n") # mostra todos os planetas e respectivos códigos

peso = int(input("peso (Kg): ")) # input do peso
planet = str(input("planet Code: ")) # input do código do planeta

match planet: # faz o cálculo e imprime para cada planeta
    case "1":
        weight = peso * 0.37
        print("your weight would be", weight, "Kg")
    case "2":
        weight = peso * 0.88
        print("your weight would be", weight, "Kg")
    case "3":
        weight = peso * 0.38
        print("your weight would be", weight, "Kg")
    case "4":
        weight = peso * 2.64
        print("your weight would be", weight, "Kg")
    case "5":
        weight = peso * 1.15
        print("your weight would be", weight, "Kg")
    case "6":
        weight = peso * 1.17
        print("your weight would be", weight, "Kg")