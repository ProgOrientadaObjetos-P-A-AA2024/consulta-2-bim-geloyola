class EstudiantePresencial(Estudiante):
    def __init__(self):
        super().__init__()
        # 1. Declarar
        self._numero_creditos = 0
        self._costo_credito = 0.0
        self._matricula_presencial = 0.0
    
    # 2. Método establecerNumeroCreditos(numero: Entero)
    def establecer_numero_creditos(self, numero):
        self._numero_creditos = numero
    
    # 3. Método establecerCostoCredito(valor: Real)
    def establecer_costo_credito(self, valor):
        self._costo_credito = valor

    # 4. Método calcularMatriculaPresencial()
    def calcular_matricula_presencial(self):
        self._matricula_presencial = self._numero_creditos * self._costo_credito
    
    # Métodos obtener para los datos o atributos de la clase
    # 5. Método obtenerNumeroCreditos() : Entero
    def obtener_numero_creditos(self):
        return self._numero_creditos
    
    # 6. Método obtenerCostoCredito() : Real
    def obtener_costo_credito(self):
        return self._costo_credito
    
    # 7. Método obtenerMatriculaPresencial() : Real
    def obtener_matricula_presencial(self):
        return self._matricula_presencial

    def __str__(self):
        return (f"Nombre: {self.obtener_nombres_estudiante()}\n"
                f"Apellido: {self.obtener_apellido_estudiante()}\n"
                f"Identificación: {self.obtener_identificacion_estudiante()}\n"
                f"Edad: {self.obtener_edad_estudiante()}\n"
                f"Número de Créditos: {self.obtener_numero_creditos()}\n"
                f"Costo por Crédito: {self.obtener_costo_credito():.2f}\n"
                f"Matricula Presencial: {self.obtener_matricula_presencial():.2f}\n")
