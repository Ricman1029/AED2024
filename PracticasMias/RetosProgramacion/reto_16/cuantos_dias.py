def contar_dias(fecha1, fecha2):
    cantidad_dias = 0
    dia1, mes1, año1 = int(fecha1[0:2]), int(fecha1[3:5]), int(fecha1[6:10])
    dia2, mes2, año2 = int(fecha2[0:2]), int(fecha2[3:5]), int(fecha2[6:10])

    treinta = (11, 4, 6, 9)
    treinta_y_uno = (12, 10, 8, 7, 5, 3, 1)

    if mes1 in treinta:
        cantidad_dias += 30 - dia1
    elif mes1 in treinta_y_uno:
        cantidad_dias += 31 - dia1
    else:
        cantidad_dias += 28 - dia1
        # Ni ganas la verdad, hay que fijarse si el año es biciesto o no asi que no lo voy a hacer




def principal():
    fecha1 = input("Ingrese la primer fecha (dd/mm/yyyy): ")
    fecha2 = input("Ingrese la segunda fecha (dd/mm/yyyy): ")

    dias = contar_dias(fecha1, fecha2)


if __name__ == '__main__':
    principal()