#	Mensaje de inicio
print('Este programa calcula el precio de un boleto de ómnibus de media distancia.')

base = float(input('Ingrese el monto base del boleto: '))
kilometros = float(input('Ingrese la cantidad de kilometros que va a recorrer: '))
adic = kilometros * 0.3
precio = base + adic

print('El precio del boleto es de: $', precio)