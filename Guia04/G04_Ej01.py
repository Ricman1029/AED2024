"""
Se desea un programa que: solicite al usuario un nombre, un apellido y el dominio y luego, proponga una dirección de
mail para el nombre y apellido ingresado de acuerdo a las siguientes reglas:
    - Componer la dirección de correo de la siguiente manera:
    <primer letra del nombre><apellido>@<dominio>
    Por ejemplo para Nombre = Felipe, Apellido = Steffolani y Dominio = frc.utn.edu.ar la dirección de mail sería:
    fsteffolani@frc.utn.edu.ar
    - Pero si la primer letra del nombre y la primera letra del apellido son la misma entonces utilizar:
    <nombre>.<apellido>@<dominio>
    Por ejemplo para Nombre = Soledad, Apellido = Steffolani y Dominio = colegiorosarito.edu.ar al dirección de mail
    sería:
    soledad.steffolani@colegiorosarito.edu.ar
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
dominio = input("Ingrese el domino: ")

if nombre[0] == apellido[0]:
    print(f"{nombre}.{apellido}@{dominio}")
else:
    print(f"{nombre[0]}{apellido}@{dominio}")
