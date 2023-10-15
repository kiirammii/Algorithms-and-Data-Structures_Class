#recebe os valores
altura = float(input("altura (m): "))
peso = float(input("peso (Kg): "))

#converte
imc = peso/pow(altura, 2)

#imprime
print("IMG: ", round(imc, 2))