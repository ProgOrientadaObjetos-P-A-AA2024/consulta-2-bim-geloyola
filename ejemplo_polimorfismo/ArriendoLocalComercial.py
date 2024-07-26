class ArriendoLocalComercial(Arriendo):
    def __init__(self, nombre, cuota_base):
        super().__init__(nombre, cuota_base)
        self.valor_adicional_fijo = 0.0

    def establecer_nombre_arrendatario(self, nombre):
        self.nombre_arrendatario = nombre.upper()  # Convierte el nombre a mayúsculas

    def establecer_valor_adicional_fijo(self, valor):
        self.valor_adicional_fijo = valor

    def establecer_arriendo_mensual(self):
        self.arriendo_mensual = self.cuota_base + self.valor_adicional_fijo

    def obtener_valor_adicional_fijo(self):
        return self.valor_adicional_fijo

    def __str__(self):
        cadena = (f"Arriendo de Local Comercial\n"
                  f"Nombre Arrendatario: {self.obtener_nombre_arrendatario()}\n"
                  f"Cuota base: {self.obtener_cuota_base():.2f}\n"
                  f"Valor adicional fijo: {self.obtener_valor_adicional_fijo():.2f}\n"
                  f"Arriendo Total: {self.obtener_arriendo_mensual():.2f}\n")
        return cadena