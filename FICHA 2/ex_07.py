print("Planet Codes\n\t1 - Mercury\n\t2 - Venus\n\t3 - Mars\n\t4 - Jupiter\n\t5 - Saturn\n\t6 - Uranus\n\n")

peso = int(input("peso (Kg): "))
planet = str(input("planet Code: "))

match planet:
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