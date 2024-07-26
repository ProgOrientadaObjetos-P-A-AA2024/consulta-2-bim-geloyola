def main():
    lista_arriendos = []

    arriendo_comida = ArriendoLocalComida("Christian Shepherd", 300)
    arriendo_comida.establecer_iva(10)  # en porcentaje
    arriendo_comida.establecer_valor_agua(20.2)  # en $
    arriendo_comida.establecer_valor_luz(40.2)  # en $

    arriendo_comercial = ArriendoLocalComercial("Andrew Schroeder", 400)
    arriendo_comercial.establecer_valor_adicional_fijo(100)  # en $

    arriendo_sesiones = ArriendoLocalSesiones("Angela Watson", 350)
    arriendo_sesiones.establecer_valor_sillas(10)  # en $
    arriendo_sesiones.establecer_valor_amplificacion(20)  # en $

    lista_arriendos.append(arriendo_comida)
    lista_arriendos.append(arriendo_comercial)
    lista_arriendos.append(arriendo_sesiones)

    for arriendo in lista_arriendos:
        arriendo.establecer_arriendo_mensual()

    centro = CentroComercial("La Pradera", lista_arriendos)
    centro.establecer_total_arriendos_base_mensual()
    centro.establecer_total_arriendos_final_mensual()

    print(centro)

if __name__ == "__main__":
    main()