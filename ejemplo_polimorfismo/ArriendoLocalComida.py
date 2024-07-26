class ArriendoLocalComida(Arriendo):
    def __init__(self, nombre, cuota_base, valor_luz=0.0, valor_agua=0.0, iva=0.0):
        super().__init__(nombre, cuota_base)
        self.valor_luz = valor_luz
        self.valor_agua = valor_agua
        self.iva = iva

    def establecer_valor_luz(self, valor):
        self.valor_luz = valor

    def establecer_valor_agua(self, valor):
        self.valor_agua = valor

    def establecer_iva(self, iva):
        self.iva = iva

    def establecer_arriendo_mensual(self):
        subtotal = self.obtener_valor_agua() + self.obtener_valor_luz() + self.obtener_cuota_base()
        self.arriendo_mensual = subtotal + (subtotal * (self.obtener_iva() / 100))

    def obtener_valor_luz(self):
        return self.valor_luz

    def obtener_valor_agua(self):
        return self.valor_agua

    def obtener_iva(self):
        return self.iva

    def __str__(self):
        cadena = (f"Arriendo de Local Comida\n"
                  f"Nombre Arrendatario: {self.obtener_nombre_arrendatario()}\n"
                  f"Cuota base: {self.obtener_cuota_base():.2f}\n"
                  f"Valor luz: {self.obtener_valor_luz():.2f}\n"
                  f"Valor agua: {self.obtener_valor_agua():.2f}\n"
                  f"Porcentaje iva: {self.obtener_iva():.2f}\n"
                  f"Arriendo Total: {self.obtener_arriendo_mensual():.2f}\n")
        return cadena