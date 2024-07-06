# mensaje de inicio y carga de datos...
print('Calcular precio al contado y con tarjeta.')
pl = float(input('Ingrese el precio de lista de un artículo: '))

# procesos...
pc = pl * 0.9
pt = pl * 1.05

# resultados...
print('Precio al contado: ', pc, '- Precio con tarjeta: ', pt)