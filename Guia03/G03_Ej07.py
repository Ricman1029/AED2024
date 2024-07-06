"""
En un hospital existen 3 áreas de servicios: Urgencias, Pediatría y Traumatología. El presupuesto anual del hospital
se reparte de la siguiente manera:

Area            Presupuesto
Urgencias       37%
Pediatría       42%
Traumatología   21%

Cargar por teclado el monto del presupuesto total del hospital, y calcular y mostrar el monto que recibirá cada área.
"""

presupuesto = float(input("Ingrese el presupuesto total del hospital: "))

urgencias = presupuesto * .37
pediatria = presupuesto * .42
traumatologia = presupuesto * .21

print(f"El área de urgencias recibirá ${urgencias}")
print(f"El área de pediatría recibirá ${pediatria}")
print(f"El área de traumatología recibirá ${traumatologia}")

