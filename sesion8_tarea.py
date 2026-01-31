#Ejercicio de tarea: 

#Determinar el promedio de N notas de un estudiante. Las notas deben alacenarse en una lista y el programa
#debe soportar las operaciones: Agregar nota, quitar nota, mostrar notas y mostrar promedio.

# Hacer Menu de operaciones con las opciones:
# 1- Agregar nota 
# 2- Quitar nota
# 3- Mostrar notas 
# 4- Mostrar promedio 
# 5- Terminar 

notas = []  # Lista para almacenar las notas del estudiante

while True:
    print("\nMenú de operaciones:")
    print("\n1. Agregar nota")
    print("2. Quitar nota")
    print("3. Mostrar notas")
    print("4. Mostrar promedio")
    print("5. Terminar")
    opcion = input("\nIngrese una opción: ") #Menu de opciones

    if opcion == "1": # Agregar nota
        nota = float(input("\nIngrese la nota a agregar: ")) # imput para agregar nota y float para permitir decimales 
        notas.append(nota) # .append para agrega la nota a la lista de notas
        print(f"Nota {nota} agregada correctamente en la actual lista de notas {notas}.") # Confirmacion de nota agregada 
        

    elif opcion == "2": # Quitar nota 
        if notas: # 
            nota_a_quitar = float(input("Ingrese la nota a quitar: ")) # input para quitar nota y float para permitir decimales
            if nota_a_quitar in notas: # Verifica si la nota a quitar está en la lista de notas
                notas.remove(nota_a_quitar) # .remove para quitar la nota de la lista de notas
                print(f"Nota {nota_a_quitar} quitada correctamente.") # Confirmacion de nota quitada
            else: # Si la nota no está en la lista
                print(f"Nota {nota_a_quitar} no encontrada.") # Mensaje de nota no encontrada
        else: # Si no hay notas en la lista
            print("No hay notas para quitar.") # Mensaje de no hay notas

    elif opcion == "3": # Mostrar notas
        if notas: # Verifica si hay notas en la lista
            print(f"Notas del estudiante: {notas}") # Muestra la lista de notas
        else: # Si no hay notas en la lista
            print("No hay notas para mostrar.") # Mensaje de no hay notas

    elif opcion == "4": # Mostrar promedio
        if notas: # Verifica si hay notas en la lista
            promedio = sum(notas) / len(notas) # Calcula el promedio de las notas, 'len' para obtener la cantidad de notas
            print(f"Promedio del estudiante: {promedio}") # Muestra el promedio de las notas
        else: # Si no hay notas en la lista
            print("No hay notas para calcular el promedio.") # Mensaje de no hay notas 

    elif opcion == "5": # Terminar
        print("Terminando el programa.") # Mensaje de terminacion del programa
        break # Sale del bucle y termina el programa

    else: # Opción inválida
        print("Opción inválida. Intente nuevamente.") # Mensaje de opcion invalida 
    
    