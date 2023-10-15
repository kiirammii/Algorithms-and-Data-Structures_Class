#recebe o valor
gender = str(input("género(M/F): "))
altura = int(input("altura(cm): "))

#verifica e imprime
if gender == 'F':
    peso = (altura-100) - (altura-150) / 2
    print("peso ideal (Kg): ", peso)
elif gender == 'M':
    peso = float((altura-100) - (altura-150) / 4)
    print("peso ideal (Kg): ", round(peso, 2))
else: print("inválido")