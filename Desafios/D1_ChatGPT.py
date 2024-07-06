def segundos_a_hms(segundos):
    # Calcula horas, minutos y segundos
    horas = segundos // 3600
    segundos_restantes = segundos % 3600
    minutos = segundos_restantes // 60
    segundos = segundos_restantes % 60

    # Verifica si las horas exceden las 24 horas
    if horas >= 24:
        return "Excedido"
    else:
        # Formatea la cadena de salida como hh:mm:ss
        return f"{horas:02}:{minutos:02}:{segundos:02}"


def hms_a_segundos(horas, minutos, segundos):
    # Convierte horas, minutos y segundos a segundos totales
    return horas * 3600 + minutos * 60 + segundos


def main():
    # Solicitar al usuario la operación deseada
    operacion = input("Escribe '1' para convertir segundos a hh:mm:ss, o '2' para convertir hh:mm:ss a segundos: ")

    if operacion == '1':
        # Convierte de segundos a hh:mm:ss
        segundos = int(input("Introduce el número de segundos: "))
        resultado = segundos_a_hms(segundos)
        print("Resultado:", resultado)
    elif operacion == '2':
        # Convierte de hh:mm:ss a segundos
        horas = int(input("Introduce las horas: "))
        minutos = int(input("Introduce los minutos: "))
        segundos = int(input("Introduce los segundos: "))
        resultado = hms_a_segundos(horas, minutos, segundos)
        print("Total de segundos:", resultado)
    else:
        print("Opción no válida.")


if __name__ == "__main__":
    main()
