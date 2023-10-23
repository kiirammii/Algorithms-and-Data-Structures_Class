#recebe o valor
lado_1 = float(input("medida do 1ºlado: "))
lado_2 = float(input("medida do 2ºlado: "))
lado_3 = float(input("medida do 3ºlado: "))

#verifica e imprime
if lado_1 == lado_2 and lado_2 == lado_3 :
    print("o triângulo é equilátero")
elif (lado_1 == lado_2 and lado_2 != lado_3) or (lado_1 == lado_3 and lado_3 != lado_2) or (lado_2 == lado_3 and lado_3 != lado_1):
    print("o triângulo é isósceles")
else: print("o triângulo é escaleno")