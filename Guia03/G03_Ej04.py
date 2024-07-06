"""
Desarrollar un programa que, conociendo el horario de partida y llegada de un vuelo (hora y minutos), determine cuál
es su duración en minutos. Si el viajero necesita luego 45 minutos más para ir del aeropuerto al hotel que ha reservado,
¿a qué hora llegará al mismo?
"""

# Se ingresan los datos
horario_partida = input("Ingrese el horario de partida del vuelo (formato hh:mm): ")
horario_llegada = input("Ingrese el horario de llegada del vuelo (formato hh:mm): ")

# Obtengo las horas y minutos de partida y llegada en base a los datos ingresados
horas_partida = int(horario_partida[0] + horario_partida[1])
minutos_partida = int(horario_partida[3] + horario_partida[4])
horas_llegada = int(horario_llegada[0] + horario_llegada[1])
minutos_llegada = int(horario_llegada[3] + horario_llegada[4])

# Se calculan los minutos de vuelo
# Horario de llegada menos horario de partida
minutos_de_vuelo = (horas_llegada * 60 + minutos_llegada) - (horas_partida * 60 + minutos_partida)

# Para calcular la hora de llegada, primero agarramos los minutos de llegada del avion y le sumamos 45min, que es lo que
# tarda el viajero en llegar del aeropuerto al hotel.
# Después calculamos las horas totales que hay en esos minutos, y el resto de la división son los minutos que faltan.
hora_llegada_hotel = (minutos_llegada + 45) // 60 + horas_llegada
minutos_llegada_hotel = (minutos_llegada + 45) % 60
horario_llegada_hotel = f"{hora_llegada_hotel}:{minutos_llegada_hotel}"

# Imprimimos los resultados.
print(f"El vuelo tiene una duración de {minutos_de_vuelo} minutos.")
print(f"El viajero llegará al hotel a las {horario_llegada_hotel}.")

