"""
Se conoce el monto del salario actual de un empleado, el nombre del empleado y el área funcional al cual pertenece.
Se pide calcular el nuevo salario del empleado sabiendo que obtuvo un incremento del 8% sobre su salario actual y un
descuento de 2.5% por servicios, informando los resultados con el formato que se especifica a continuación:
Nombre Empleado:  xxxxxxxxx         Nuevo Salario: $ xxx

Área Funcional:  xxxxxxxxxxxx

Salario Actual: $ xxxx
"""

nombre = input("Ingrese el nombre del empleado: ")
area_funcional = input("Ingrese el área funcional del empleado: ")
salario_actual = float(input("Ingrese el salario actual del empleado: "))

# Calculamos un aumento del 8% y sobre ese aumento, un descuento del 2.5%
nuevo_salario = salario_actual * 1.08 * 0.975

print(f"Nombre Empleado: {nombre}\tNuevo Salario: ${nuevo_salario}")
print(f"Área Funcional: {area_funcional}")
print(f"Salario Actual: ${salario_actual}")
