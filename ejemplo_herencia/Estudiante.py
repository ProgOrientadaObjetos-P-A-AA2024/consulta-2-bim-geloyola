class Estudiante:
    def __init__(self):
        # 1.  Declarar
        # se declaran datos o atributos con visibilidad protegido
        # # nombresEstudiante: Cadena
        self._nombres_estudiante = ""
        # # apellidosEstudiante: Cadena
        self._apellidos_estudiante = ""
        # # identificacionEstudiante: Cadena
        self._identificacion_estudiante = ""
        # # edadEstudiante: Entero
        self._edad_estudiante = 0

    #  Métodos establecer y calcular para los datos o atributos de la clase
    
    # 2.  Método establecerNombresEstudiante(nom: Cadena)
    def establecer_nombres_estudiante(self, nom):
        self._nombres_estudiante = nom
    
    # 3.  Método establecerApellidoEstudiante(ape: Cadena)
    def establecer_apellido_estudiante(self, ape):
        self._apellidos_estudiante = ape
    
    # 4.  Método establecerIdentificacionEstudiante(iden: Cadena)
    def establecer_identificacion_estudiante(self, iden):
        self._identificacion_estudiante = iden

    # 5.  Método establecerEdadEstudiante(ed: Edad)
    def establecer_edad_estudiante(self, ed):
        self._edad_estudiante = ed
    
    #  Métodos obtener para los datos o atributos de la clase
    # 6.  Método obtenerNombresEstudiante() : Cadena
    def obtener_nombres_estudiante(self):
        return self._nombres_estudiante
    
    # 7.  Método obtenerApellidoEstudiante() : Cadena
    def obtener_apellido_estudiante(self):
        return self._apellidos_estudiante
    
    # 8. Método obtenerIdentificacionEstudiante() : Cadena
    def obtener_identificacion_estudiante(self):
        return self._identificacion_estudiante
    
    # 9.  Método obtenerEdadEstudiante() : Entero
    def obtener_edad_estudiante(self):
        return self._edad_estudiante
