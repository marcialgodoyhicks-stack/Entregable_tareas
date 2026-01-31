# Usando Python como lenguaje, crea un programa que permita gestionar el inventario de una bodega 
# La bodega almacena artículos de los que se desea registrar para cada tipo 
# de artículo el código numérico interno, el nombre del artículo, la cantidad de 
# unidades en existencia (stock) y el nombre de la unidad o departamento de 
# la empresa que lo dejó almacenado. 

# Considera los siguientes requisitos:
#   • Los datos de los artículos deben ser almacenados en una lista de listas o 
#   en una lista de diccionarios (sólo para valientes).
#   • El programa debe permitir el ingreso y la eliminación de artículos. 
#   También debe permitir la búsqueda de un artículo mediante el código 
#   interno y la modificación del stock.
#   • Las opciones deben presentarse mediante un menú.


# Se crea una lista vacía donde se guardarán todos los artículos de la bodega
lista_articulos = []

# Bucle infinito para que el menú se repita hasta que el usuario decida salir
while True:

    # Se muestran las opciones del menú en pantalla
    print("\n--- MENÚ BODEGA ---") # \n Para saltar una linea en la terminal 
    print("1. Ingresar artículo")
    print("2. Eliminar artículo")
    print("3. Buscar artículo por código")
    print("4. Modificar stock")
    print("5. Mostrar inventario")
    print("6. Salir")

    # Se solicita al usuario que ingrese una opción del menú con input y la variable 'opcion'
    opcion = input("Seleccione una opción: ")

    # Si el usuario elige la opción 1 (ingresar artículo)
    if opcion == "1":

        # Se solicita el código del artículo y se convierte a entero con 'int'
        codigo = int(input("Ingrese código del artículo: "))

        # Se solicita el nombre del artículo (texto)
        nombre = input("Ingrese nombre del artículo: ") 

        # Se solicita la cantidad de stock y se convierte a entero
        stock = int(input("Ingrese stock: "))

        # Se solicita el nombre del departamento que dejó el artículo
        departamento = input("Ingrese departamento: ")

        # Se crea un diccionario con los datos del artículo ingresado
        articulo = {
            "codigo": codigo,           # Clave 'codigo' guarda el valor ingresado
            "nombre": nombre,           # Clave 'nombre' guarda el nombre del artículo
            "stock": stock,             # Clave 'stock' guarda la cantidad disponible
            "departamento": departamento # Clave 'departamento' guarda el origen
        }

        # Se agrega el diccionario a la lista de artículos
        lista_articulos.append(articulo)

        # Se informa que el artículo fue ingresado correctamente
        print("Artículo ingresado correctamente.")

    # Si el usuario elige la opción 2 (eliminar artículo)
    elif opcion == "2":

        # Se solicita el código del artículo a eliminar
        codigo = int(input("Ingrese código del artículo a eliminar: "))

        # Variable bandera para saber si el artículo fue encontrado
        encontrado = False

        # Se recorre la lista de artículos
        for articulo in lista_articulos:

            # Se compara el código ingresado con el código del artículo
            if articulo["codigo"] == codigo:

                # Si coincide, se elimina el artículo de la lista
                lista_articulos.remove(articulo)

                # Se marca que el artículo fue encontrado
                encontrado = True

                # Se informa que el artículo fue eliminado
                print("Artículo eliminado.")

                # Se sale del ciclo porque ya se encontró el artículo
                break

        # Si terminó el ciclo y no se encontró el artículo
        if not encontrado:
            print("Artículo no encontrado.")

    # Si el usuario elige la opción 3 (buscar artículo)
    elif opcion == "3":

        # Se solicita el código del artículo a buscar
        codigo = int(input("Ingrese código del artículo a buscar: "))

        # Variable bandera para saber si el artículo existe
        encontrado = False

        # Se recorre la lista de artículos
        for articulo in lista_articulos:

            # Se verifica si el código coincide
            if articulo["codigo"] == codigo:

                # Se muestra el artículo encontrado
                print(articulo)

                # Se marca como encontrado
                encontrado = True

                # Se sale del ciclo
                break

        # Si no se encontró el artículo
        if not encontrado:
            print("Artículo no encontrado.")

    # Si el usuario elige la opción 4 (modificar stock)
    elif opcion == "4":

        # Se solicita el código del artículo
        codigo = int(input("Ingrese código del artículo: "))

        # Variable para controlar si se encontró el artículo
        encontrado = False

        # Se recorre la lista de artículos
        for articulo in lista_articulos:

            # Se compara el código
            if articulo["codigo"] == codigo:

                # Se solicita el nuevo stock
                nuevo_stock = int(input("Ingrese nuevo stock: "))

                # Se actualiza el stock del artículo
                articulo["stock"] = nuevo_stock

                # Se marca como encontrado
                encontrado = True

                # Se informa que el stock fue actualizado
                print("Stock actualizado.")

                # Se sale del ciclo
                break

        # Si el artículo no fue encontrado
        if not encontrado:
            print("Artículo no encontrado.")

    # Si el usuario elige la opción 5 (mostrar inventario)
    elif opcion == "5":

        # Si la lista está vacía
        if len(lista_articulos) == 0:
            print("Inventario vacío.")

        # Si hay artículos registrados
        else:
            # Se recorren todos los artículos y se muestran
            for articulo in lista_articulos:
                print(articulo)

    # Si el usuario elige la opción 6 (salir del programa)
    elif opcion == "6":

        # Se muestra mensaje de salida
        print("Saliendo del programa...")

        # Se rompe el bucle while y termina el programa
        break

    # Si el usuario ingresa una opción inválida
    else:
        print("Opción no válida.")
