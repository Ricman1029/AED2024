"""
Ingresar por teclado las edades de 3 participantes de un concurso.
Informar si todos cumplen con la edad mínima establecida para el mismo, también ingresada por teclado.
"""

participante1 = int(input("Edad del primer participante: "))
participante2 = int(input("Edad del segundo participante: "))
participante3 = int(input("Edad del tercer participante: "))
edad_establecida = int(input("Ingresar la edad mínima permitida: "))

if participante1 >= edad_establecida and participante2 >= edad_establecida and participante3 >= edad_establecida:
    respuesta = "Todos los participantes cumplen con el requisito de edad."
else:
    respuesta = "No todos los participantes cumplen con el requisito de edad."

print(respuesta)

