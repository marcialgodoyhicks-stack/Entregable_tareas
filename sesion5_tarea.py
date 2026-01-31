# Ingreso de notas
# Se crea una variable para la nota 1, utilizando 
#un float para decimales e input para ingresar la nota. 

EVS1 = float(input("Ingrese la primera nota: "))
EVS2 = float(input("Ingrese la segunda nota: "))
EVS3 = float(input("Ingrese la tercera nota: "))


# Cálculo del promedio
# Se crea la variable y se cálcula la nota 
promedio = (EVS1 + EVS2 + EVS3) / 3

# Evaluación del resultado
if promedio >= 5.0: #Se utiliza un if como condicionante para la variable promedio igual o mayor a 5. 
    print(f"Promedio final: {promedio:.2f}") #se imprime el promedio y se utiliza un f para concatenar texto y variables en el código 
    print("¡Aprobado!") # se imprime el mensaje aprobado según la condicionante anterior. 
elif promedio >= 4.0: # identicamente lo mismo hacia abajo según las nuevas condicionantes por promedio de notas. 
    print(f"Promedio final: {promedio:.2f}")
    print("¡Va a examen!")
else:
    print(f"Promedio final: {promedio:.2f}")
    print("¡Reprobado!")
