"""
Desarrollar un programa que cargue por teclado la cantidad de dinero depositada en plazo fijo por un cliente de un banco
y calcular el saldo que tendrá esa cuenta al vencer el plazo fijo, sabiendo que el interés pactado era de 2.3% y que el
banco cobra una tasa fija de gastos por servicios financieros igual a $20 por cuenta.
"""

deposito = float(input("Ingrese la cantidad de dinero a depositar: "))
saldo = deposito * 1.023 - 20

print(f"El saldo al vencer el plazo fijo será de ${saldo}.")
