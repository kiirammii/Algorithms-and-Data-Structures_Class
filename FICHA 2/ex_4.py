#recebe os valores
altura = float(input("altura (m): "))
peso = float(input("peso (Kg): "))

#converte
imc = float(peso/pow(altura, 2))

# valida e imprime
if imc < 18.5:
    print("Underweight")
elif imc >= 18.5 and imc < 25:
    print("Healthy")
elif imc >= 25 and imc < 30:
    print("Overweight")
elif imc >= 30 and imc < 35:
    print("Obesity Grade I")
elif imc >= 35 and imc < 40:
    print("Obesity Grade II (severe)")
elif imc >= 40:
    print("Obesity Grade III (morbid)")
else: print ("error")