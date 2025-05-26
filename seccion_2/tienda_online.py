#Tienda Online
array_productos = [
    {
        "id": 1,
        "nombre": "Laptop",
        "precio": 800.00,
        "cantidad": 10,
        "disponible": True,
    },
    {
        "id": 2,
        "nombre": "Smartphone",
        "precio": 500.00,
        "cantidad": 20,
        "disponible": True,
    },
    {
        "id": 3,
        "nombre": "Tablet",
        "precio": 300.00,
        "cantidad": 15,
        "disponible": True,
    },
    {
        "id": 4,
        "nombre": "Smartwatch",
        "precio": 200.00,
        "cantidad": 5,
        "disponible": False,
    }
]
continuar = True
print("Bienvenido a nuestra tienda online")

while continuar:
    try:
        case = int(input("\nIngrese el ID del producto que desea editar (1-4) o (6) para salir: "))
        if  1 >= case <= 4 :
            producto = array_productos[case - 1]
            print(f"\nUsted ha seleccionado el {producto['nombre']}")
            print(f"Precio: ${producto['precio']}")
            print(f"Cantidad disponible: {producto['cantidad']}") 
            print(f"Disponible: {'Sí' if producto['disponible'] else 'No'}")
            print("¿Desea editar este producto? (sí/no)")
            editar = input().strip().lower()
            if editar == "sí" or editar == "si":
                nombre = input(f"Ingrese el nuevo nombre del producto (actual: {producto['nombre']}): ")
                precio = float(input(f"Ingrese el nuevo precio (actual: ${producto['precio']}): "))
                cantidad = int(input(f"Ingrese la nueva cantidad disponible (actual: {producto['cantidad']}): "))
                disponible_input = input(f"¿Está disponible? (actual: {'Sí' if producto['disponible'] else 'No'}) [sí/no]: ").strip().lower()

                # Asignar cambios
                producto["nombre"] = nombre
                producto["precio"] = precio
                producto["cantidad"] = cantidad
                producto["disponible"] = disponible_input == "sí" or disponible_input == "si"
            else:
                print("No se realizaron cambios en el producto.")
        elif case == 6:
            print("Saliendo de la tienda online. ¡Gracias por visitarnos!")
            continuar = False
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número entero.")