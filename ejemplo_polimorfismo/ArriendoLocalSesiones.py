class ArriendoLocalSesiones(Arriendo):
    def __init__(self, nombre, cuota_base):
        super().__init__(nombre, cuota_base)
        self.valor_sillas = 0.0
        self.valor_amplificacion = 0.0

    def establecer_valor_sillas(self, valor):
        self.valor_sillas = valor

    def establecer_valor_amplificacion(self, valor):
        self.valor_amplificacion = valor

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = self.obtener_cuota_base() + self.obtener_valor_sillas() + self.obtener_valor_amplificacion()

    def obtener_valor_sillas(self):
        return self.valor_sillas

    def obtener_valor_amplificacion(self):
        return self.valor_amplificacion

    def __str__(self):
        cadena = (f"Arriendo de Local Sesiones\n"
                  f"Nombre Arrendatario: {self.obtener_nombre_arrendatario()}\n"
                  f"Cuota base: {self.obtener_cuota_base():.2f}\n"
                  f"Valor sillas: {self.obtener_valor_sillas():.2f}\n"
                  f"Valor amplificación: {self.obtener_valor_amplificacion():.2f}\n"
                  f"Arriendo Total: {self.obtener_arriendo_mensual():.2f}\n")
        return cadena