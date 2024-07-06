eleccion = input("Ingrese '0' para convertir de segundos a hh:mm:ss."
                 "\nIngrese algo distinto de '0' para convertir de hh:mm:ss a segundos.\n")

if eleccion == '0':
    segundos = float(input('Ingrese la cantidad de segundos que desea convertir al formato hh:mm:ss: '))

    horas = segundos // 3600
    minutos = segundos % 3600 // 60
    segundos = segundos % 3600 % 60

    if horas > 24:
        print("Excedido")
    else:
        print(str(horas) + ':' + str(minutos) + ':' + str(segundos))
else:
    print("A continuación deberá ingresar una cantidad de horas, minutos y segundos para convertirlos a solo segundos.")
    horas = int(input("Horas: "))
    minutos = int(input("Minutos: "))
    segundos = int(input("Segundos: "))

    segundos = segundos + horas * 3600 + minutos * 60
    print(segundos)
