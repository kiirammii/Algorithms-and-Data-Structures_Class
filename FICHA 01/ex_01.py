#recebe os valores
pol = int(input("medida (pol):"))

#converte
medida_mm = pol*25.4
medida_cm = medida_mm / 10

#imprime
print ("medida (cm): ", medida_cm, "cm")
print ("medida (mm): ", medida_mm, "mm")