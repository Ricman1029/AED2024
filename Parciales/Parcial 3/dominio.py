class Juicio:
    def __init__(self, codigo_expediente, descripcion, tipo, cliente, honorarios):
        self.codigo_expediente = codigo_expediente
        self.descripcion = descripcion
        self.tipo = tipo
        self.cliente = cliente
        self.honorarios = honorarios

    def __str__(self):
        return (f"Código: {self.codigo_expediente} - Descripción: {self.descripcion} - Tipo: {self.tipo} - "
                f"Cliente: {self.cliente} - Honorarios: {self.honorarios}")