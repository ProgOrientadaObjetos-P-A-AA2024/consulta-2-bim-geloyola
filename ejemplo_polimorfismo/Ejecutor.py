class Arriendo:
    def establecerArriendoMensual(self):
        raise NotImplementedError("Este método debe ser implementado por una subclase")

class ArriendoLocalComida(Arriendo):
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.iva = 0
        self.valor_agua = 0
        self.valor_luz = 0

    def establecerIva(self, iva):
        self.iva = iva

    def establecerValorAgua(self, valor_agua):
        self.valor_agua = valor_agua

    def establecerValorLuz(self, valor_luz):
        self.valor_luz = valor_luz

    def establecerArriendoMensual(self):
        self.arriendo_mensual = self.valor + (self.valor * self.iva / 100) + self.valor_agua + self.valor_luz

    def __str__(self):
        return f"ArriendoLocalComida(nombre={self.nombre}, valor={self.valor}, iva={self.iva}, valor_agua={self.valor_agua}, valor_luz={self.valor_luz}, arriendo_mensual={self.arriendo_mensual})"

class ArriendoLocalComercial(Arriendo):
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.valor_adicional_fijo = 0

    def establecerValorAdicionalFijo(self, valor_adicional_fijo):
        self.valor_adicional_fijo = valor_adicional_fijo

    def establecerArriendoMensual(self):
        self.arriendo_mensual = self.valor + self.valor_adicional_fijo

    def __str__(self):
        return f"ArriendoLocalComercial(nombre={self.nombre}, valor={self.valor}, valor_adicional_fijo={self.valor_adicional_fijo}, arriendo_mensual={self.arriendo_mensual})"

class ArriendoLocalSesiones(Arriendo):
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        self.valor_sillas = 0
        self.valor_amplificacion = 0

    def establecerValorSillas(self, valor_sillas):
        self.valor_sillas = valor_sillas

    def establecerValorAmplificacion(self, valor_amplificacion):
        self.valor_amplificacion = valor_amplificacion

    def establecerArriendoMensual(self):
        self.arriendo_mensual = self.valor + self.valor_sillas + self.valor_amplificacion

    def __str__(self):
        return f"ArriendoLocalSesiones(nombre={self.nombre}, valor={self.valor}, valor_sillas={self.valor_sillas}, valor_amplificacion={self.valor_amplificacion}, arriendo_mensual={self.arriendo_mensual})"

def main():
    lista_arriendos = []

    arriendo_comida = ArriendoLocalComida("Christian Shepherd", 300)
    arriendo_comida.establecerIva(10)
    arriendo_comida.establecerValorAgua(20.2)
    arriendo_comida.establecerValorLuz(40.2)

    arriendo_comida2 = ArriendoLocalComida("Christian Cruz", 300)
    arriendo_comida2.establecerIva(10)
    arriendo_comida2.establecerValorAgua(20.2)
    arriendo_comida2.establecerValorLuz(40.2)

    arriendo_comercial = ArriendoLocalComercial("Andrew Schroeder", 400)
    arriendo_comercial.establecerValorAdicionalFijo(100)

    arriendo_sesiones = ArriendoLocalSesiones("Angela Watson", 350)
    arriendo_sesiones.establecerValorSillas(10)
    arriendo_sesiones.establecerValorAmplificacion(20)

    lista_arriendos.append(arriendo_comida)
    lista_arriendos.append(arriendo_comida2)
    lista_arriendos.append(arriendo_comercial)
    lista_arriendos.append(arriendo_sesiones)

    for arriendo in lista_arriendos:
        arriendo.establecerArriendoMensual()
        print(arriendo)
        print()

if __name__ == "__main__":
    main()
