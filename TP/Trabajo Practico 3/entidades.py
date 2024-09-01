class Envio:

    def __init__(self, codigo_postal=0, direccion="", tipo=0, forma_pago=1):
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.tipo = tipo
        self.forma_pago = forma_pago

    def __str__(self):
        cadena = f"{self.codigo_postal}, {self.direccion}, {self.forma_pago}, {self.tipo}"
        return cadena
