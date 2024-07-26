from abc import ABC, abstractmethod

class Arriendo(ABC):
    def __init__(self, nombre, cuota_base):
        self.nombre_arrendatario = nombre
        self.cuota_base = cuota_base
        self.arriendo_mensual = 0.0

    def establecer_nombre_arrendatario(self, nombre):
        self.nombre_arrendatario = nombre

    def establecer_cuota_base(self, cuota_base):
        self.cuota_base = cuota_base

    @abstractmethod
    def establecer_arriendo_mensual(self):
        pass

    def obtener_nombre_arrendatario(self):
        return self.nombre_arrendatario

    def obtener_cuota_base(self):
        return self.cuota_base

    def obtener_arriendo_mensual(self):
        return self.arriendo_mensual