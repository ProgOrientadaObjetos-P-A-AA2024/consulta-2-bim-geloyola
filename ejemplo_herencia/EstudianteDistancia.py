class EstudianteDistancia(Estudiante):
    def __init__(self):
        super().__init__()
        # 1.  Declarar
        self._numero_asignaturas = 0
        self._costo_asignatura = 0.0
        self._matricula_distancia = 0.0
    
    # 2.  Método establecerNumeroAsignaturas(numero: Entero)
    def establecer_numero_asignaturas(self, numero):
        self._numero_asignaturas = numero
    
    # 3.  Método establecerCostoAsignatura(valor: Real)
    def establecer_costo_asignatura(self, valor):
        self._costo_asignatura = valor

    # 4.  Método calcularMatriculaDistancia()
    def calcular_matricula_distancia(self):
        self._matricula_distancia = self._numero_asignaturas * self._costo_asignatura
    
    #  Métodos obtener para los datos o atributos de la clase
    # 5. Método obtenerNumeroAsignaturas() : Entero
    def obtener_numero_asignaturas(self):
        return self._numero_asignaturas
    
    # 6. Método obtenerCostoAsignatura() : Real
    def obtener_costo_asignatura(self):
        return self._costo_asignatura
    
    # 7. Método obtenerMatriculaDistancia() : Real
    def obtener_matricula_distancia(self):
        return self._matricula_distancia
