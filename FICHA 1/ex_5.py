#recebe os valores
tempo = int(input("tempo (s): "))

#conversão
horas = int(tempo/3600)
resto = tempo % 3600

minutos = int(resto / 60)
segundos = resto % 60

#imprime o tempo em horas minutos e segundos
print(horas, "h", minutos, "m", segundos, "s")