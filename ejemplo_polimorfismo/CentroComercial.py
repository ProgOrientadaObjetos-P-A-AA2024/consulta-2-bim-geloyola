class CentroComercial:
    def __init__(self, nombre, arriendos):
        self.nombre = nombre
        self.arriendos = arriendos
        self.total_arriendos_final_mensual = 0.0
        self.total_arriendos_base_mensual = 0.0

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def establecer_arriendos(self, arriendos):
        self.arriendos = arriendos

    def establecer_total_arriendos_final_mensual(self):
        self.total_arriendos_final_mensual = sum(arriendo.obtener_arriendo_mensual() for arriendo in self.arriendos)

    def establecer_total_arriendos_base_mensual(self):
        self.total_arriendos_base_mensual = sum(arriendo.obtener_cuota_base() for arriendo in self.arriendos)

    def obtener_nombre(self):
        return self.nombre

    def obtener_arriendos(self):
        return self.arriendos

    def obtener_total_arriendos_final_mensual(self):
        return self.total_arriendos_final_mensual

    def obtener_total_arriendos_base_mensual(self):
        return self.total_arriendos_base_mensual

    def __str__(self):
        cadena = f"Datos Centro Comercial\nNombre: {self.obtener_nombre()}\nLista de Locales\n\n"
        for arriendo in self.obtener_arriendos():
            cadena += f"{arriendo}\n"
        cadena += (f"\nTotal Arriendos base Mensual: {self.obtener_total_arriendos_base_mensual():.2f}\n"
                   f"Total Arriendos Mensual: {self.obtener_total_arriendos_final_mensual():.2f}\n")
        return cadena