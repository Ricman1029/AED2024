"""
Se vota una ley en el Senado, y se ingresan votos a favor, en contra y abstenciones de los senadores presentes.

Informar cuál fue el resultado de la votación. Si la ley fue aprobada, indicar si fue por mayoría absoluta (los votos
afirmativos superan a la suma de los negativos más las abstenciones) o por mayoría simple (los votos afirmativos superan
a los negativos, sin tener en cuenta las abstenciones).

También informar en caso de que la ley sea rechazada.
Por último, considerando que la Cámara está formadad por 72 senadores, determinar cuantos se encontraban ausentes.
"""

# Se ingresan los votos de los senadores
favor = int(input("Ingrese la cantidad de votos a favor: "))
contra = int(input("Ingrese la cantidad de votos en contra: "))
abstencion = int(input("Ingrese la cantidad de abstenciones: "))

# Informar si la ley fue aprobada (de manera absoluta o simple) o si fue rechazada
if favor > contra + abstencion:
    print("La ley se aprobó por mayoría absoluta.")
elif favor > contra:
    print("La ley se aprobó por mayoría simple.")
else:
    print("La ley fue rechazada.")

# Se calcula la cantidad de ausentes en base a la cantidad de votos y un total de 72 senadores
ausentes = 72 - (favor + contra + abstencion)
print(f"La cantidad de senadores ausentes es {ausentes}")
