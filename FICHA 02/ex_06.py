#recebe o valor
gender = str(input("género(M/F): "))
age = int(input("age: "))

#verifica e imprime
if gender == 'F':
    mhr = 226 - age
    print("MHR: ", mhr)
elif gender == 'M':
    mhr = 220 - age
    print("MHR: ", mhr)
else: print("inválido")