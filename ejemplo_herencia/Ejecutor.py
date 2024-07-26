def main():
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    nombres_est = ""
    apellidos_est = ""
    identificacion_est = ""
    edad_est = 0
    costo_cred = 0.0
    numero_creds = 0
    costo_asig = 0.0
    numero_asigs = 0
    tipo_estudiante = 0
    continuar = "SI"

    while continuar.upper() == "S":
        print("Tipo de Estudiante a ingresar.\n1) Estudiante Presencial.\n2) Estudiante Distancia")
        tipo_estudiante = int(input())

        if tipo_estudiante == 1 or tipo_estudiante == 2:
            nombres_est = input("Ingrese el nombre del estudiante: ")
            apellidos_est = input("Ingrese el apellido del estudiante: ")
            identificacion_est = input("Ingrese la identificación del estudiante: ")
            edad_est = int(input("Ingrese la edad del estudiante: "))

            if tipo_estudiante == 1:
                from estudiante_presencial import EstudiantePresencial

                numero_creds = int(input("Ingrese el número de créditos del estudiante: "))
                costo_cred = float(input("Ingrese el costo de cada crédito del estudiante: "))

                estudiante_p = EstudiantePresencial()
                estudiante_p.establecer_nombres_estudiante(nombres_est)
                estudiante_p.establecer_apellido_estudiante(apellidos_est)
                estudiante_p.establecer_identificacion_estudiante(identificacion_est)
                estudiante_p.establecer_edad_estudiante(edad_est)
                estudiante_p.establecer_numero_creditos(numero_creds)
                estudiante_p.establecer_costo_credito(costo_cred)
                estudiante_p.calcular_matricula_presencial()

                print("Datos del estudiante Presencial")
                print(f"Nombre: {estudiante_p.obtener_nombres_estudiante()}")
                print(f"Apellido: {estudiante_p.obtener_apellido_estudiante()}")
                print(f"Identificación: {estudiante_p.obtener_identificacion_estudiante()}")
                print(f"Edad: {estudiante_p.obtener_edad_estudiante()}")
                print(f"Matricula final $: {estudiante_p.obtener_matricula_presencial():.2f}")

            else:
                from estudiante_distancia import EstudianteDistancia

                numero_asigs = int(input("Ingrese el número de asignaturas del estudiante: "))
                costo_asig = float(input("Ingrese el costo de cada asignatura del estudiante: "))

                estudiante_d = EstudianteDistancia()
                estudiante_d.establecer_nombres_estudiante(nombres_est)
                estudiante_d.establecer_apellido_estudiante(apellidos_est)
                estudiante_d.establecer_identificacion_estudiante(identificacion_est)
                estudiante_d.establecer_edad_estudiante(edad_est)
                estudiante_d.establecer_numero_asignaturas(numero_asigs)
                estudiante_d.establecer_costo_asignatura(costo_asig)
                estudiante_d.calcular_matricula_distancia()

                print("Datos del estudiante a Distancia")
                print(f"Nombre: {estudiante_d.obtener_nombres_estudiante()}")
                print(f"Apellido: {estudiante_d.obtener_apellido_estudiante()}")
                print(f"Identificación: {estudiante_d.obtener_identificacion_estudiante()}")
                print(f"Edad: {estudiante_d.obtener_edad_estudiante()}")
                print(f"Matricula: {estudiante_d.obtener_matricula_distancia():.2f}")

        else:
            print("Error en la opción")

        continuar = input("Desea ingresar más estudiantes. Digite la letra S para continuar o digite la letra N para salir: ")

if __name__ == "__main__":
    main()
