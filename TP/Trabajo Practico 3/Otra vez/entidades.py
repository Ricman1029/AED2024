class Envio:
    def __init__(self, codigo_postal, direccion, tipo, forma_pago):
        self.codigo_postal = codigo_postal
        self.direccion = direccion
        self.tipo = tipo
        self.forma_pago = forma_pago

    def __str__(self):
        return f"Código Postal: {self.codigo_postal} - Dirección: {self.direccion} - Tipo: {self.tipo} - Forma de pago: {self.forma_pago}"
