class Insumo:
    def __init__(self, cod=24, nom='Ricardo', pre=10.5, cant=3):
        self.codigo = cod
        self.nombre = nom
        self.valor = pre
        self.cantidad = cant

    def __str__(self):
        r = f"{self.codigo}, {self.nombre}"
        return r


def main():
    persona = Insumo()

    codigo = input("Codigo: ")
    nombre = input("Nombre: ")
    valor = input("Valor: ")
    cantidad = input("Cantidad: ")

    print(persona)

    persona.codigo = codigo
    persona.nombre = nombre
    persona.valor = valor
    persona.cantidad = cantidad

    print(persona)


if __name__ == '__main__':
    main()
