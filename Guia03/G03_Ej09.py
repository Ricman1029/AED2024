"""
Una pequeña empresa de informática tiene que desarrollar un sistema de infromación y para ello tiene un presupuesto de
x pesos para cubrir los costos de crear el sistema. Sabiendo que tiene pensado ganar al menos 17% por el proyecto,
determina cuál es el valor máximo que pueden alcanzar los costos del proyecto.
"""

# Ganancia mínima del proyecto en porcentaje
GANANCIA = 17

# Se pide ingresar el presupuesto
presupuesto = float(input("Ingrese el presupuesto: "))

# Calcular el valor maximo de los costos para el proyecto
valor_max_costo = presupuesto * ((100 - GANANCIA) / 100)

# Mostramos el resultado
print(f"Para una ganancia de mínima de {GANANCIA}% el valor maximo de los costos es de: ${valor_max_costo}")
