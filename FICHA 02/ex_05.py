numero_1 = int(input("1º número: "))
numero_2 = int(input("2º número: "))
numero_3 = int(input("3º número: "))

#verifica e imprime
if numero_1 >= numero_2 and numero_2 >= numero_3 : # 1 2 3
    print(numero_3, numero_2, numero_1)
elif numero_1 >= numero_2 and numero_1 >= numero_3 and numero_3 >= numero_2 : # 1 3 2
    print(numero_2, numero_3, numero_1)
elif numero_2 >= numero_1 and numero_2 >= numero_3 and numero_1 >= numero_3 : # 2 1 3
    print(numero_3, numero_1, numero_2)
elif numero_2 >= numero_1 and numero_2 >= numero_3 and numero_3 >= numero_1 : # 2 3 1
    print(numero_1, numero_3, numero_2)
elif numero_3 >= numero_1 and numero_3 >= numero_2 and numero_1 >= numero_2 : # 3 1 2
    print(numero_2, numero_1, numero_3)
elif numero_3 >= numero_1 and numero_3 >= numero_2 and numero_2 >= numero_1 : # 3 2 1
    print(numero_1, numero_2, numero_3)