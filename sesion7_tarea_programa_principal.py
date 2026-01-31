import sesion7_tarea_funciones

print("Inicio del programa")

while True:
    print("\nMenú de opciones")
    print("1 - Calcular área de un triángulo")
    print("2 - Calcular área de un círculo")
    print("3 - Salir")

    opcion = int(input("Ingrese una opción (1, 2, 3): "))

    if opcion == 1:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))

        area_triangulo = sesion7_tarea_funciones.area_triangulo(base, altura)

        print("El área del triángulo es:", area_triangulo)

    elif opcion == 2:
        radio = float(input("Ingrese el radio del círculo: "))

        area_circulo = sesion7_tarea_funciones.area_circulo(radio)

        print("El área del círculo es:", area_circulo)

    elif opcion == 3:
        print("Fin del programa")
        break

    else:
        print("Error: opción incorrecta")

