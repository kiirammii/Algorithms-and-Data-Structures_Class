#recebe os valores
tempo = int(input("tempo (s): "))

#conversão
horas = int(tempo/3600)
resto = tempo % 3600

minutos = int(resto / 60)
segundos = resto % 60

#imprime
print(horas, "h", minutos, "m", segundos, "s")