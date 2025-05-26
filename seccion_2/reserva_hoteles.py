# Reserva de hoteles
continuar = True
array_hoteles = [
    {
        "id": 1,
        "nombre": "Hotel Playa Dorada",
        "dias": 5,
        "precio_por_noche": 100,
        "vista_maritima": True,
    },
    {
        "id": 2,
        "nombre": "Hotel Montaña Verde",
        "dias": 3,
        "precio_por_noche": 80,
        "vista_maritima": False,
    },
    {
        "id": 3,
        "nombre": "Hotel Ciudad Dorada",
        "dias": 7,
        "precio_por_noche": 120,
        "vista_maritima": True,
    },
    {
        "id": 4,
        "nombre": "Hotel Bosque Encantado",
        "dias": 4,
        "precio_por_noche": 90,
        "vista_maritima": False,
    },
]

print("Bienvenido a nuestro sistema de reservas de hoteles")

while continuar:
    try:
        case = int(input("\nIngrese el ID del hotel (1-4), (0) para ver todos, (5) para editar, o (6) para salir: "))
        if 1 <= case <= 4:
            hotel = array_hoteles[case - 1]
            print(f"\nUsted ha seleccionado el {hotel['nombre']}")
            print(f"Días de estancia: {hotel['dias']}")
            print(f"Precio por noche: ${hotel['precio_por_noche']}")
            print(f"Vista marítima: {'Sí' if hotel['vista_maritima'] else 'No'}")

        elif case == 5:
            id_editar = int(input("Ingrese el ID del hotel que desea editar (1-4): "))
            if 1 <= id_editar <= 4:
                hotel = array_hoteles[id_editar - 1]
                nombre = input(f"Ingrese el nuevo nombre del hotel (actual: {hotel['nombre']}): ")
                dias = int(input(f"Ingrese el nuevo número de días de estancia (actual: {hotel['dias']}): "))
                precio_por_noche = float(input(f"Ingrese el nuevo precio por noche (actual: ${hotel['precio_por_noche']}): "))
                vista_maritima_input = input(f"¿Tiene vista marítima? (actual: {'Sí' if hotel['vista_maritima'] else 'No'}) [sí/no]: ").strip().lower()

                # Asignar cambios
                hotel["nombre"] = nombre
                hotel["dias"] = dias
                hotel["precio_por_noche"] = precio_por_noche
                hotel["vista_maritima"] = vista_maritima_input == "sí" or vista_maritima_input == "si"

                print("Reserva actualizada correctamente.")
            else:
                print("ID de hotel no válido.")
        elif case == 0:
            print("\nLista de hoteles disponibles:")
            for hotel in array_hoteles:
                print(f"ID: {hotel['id']}\n, Nombre: {hotel['nombre']}\n, Días: {hotel['dias']}\n, Precio por noche: ${hotel['precio_por_noche']}\n, Vista marítima: {'Sí' if hotel['vista_maritima'] else 'No'}\n")
        elif case == 6:
            print("Gracias por usar nuestro sistema de reservas. ¡Hasta luego!")
            continuar = False
        else:
            print("Opción no válida. Por favor, ingrese un número entre 1 y 6.")

    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")
