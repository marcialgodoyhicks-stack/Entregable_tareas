#Ejercicio de tarea: conversión de grados celcius a fahrenheit (Investigar la formula)

# Conversión de grados Celsius a Fahrenheit 

celsius = input("Ingresa la temperatura en grados Celsius: ") # input para ingresar la temperatura
celsius = float(celsius) # Se crea una variable y se utiliza un float para permitir decimales 
fahrenheit = (celsius * 9/5) + 32 # se crea la carible y con la formula a calcular 
print(f"La temperatura en Fahrenheit es: {fahrenheit}") # Se imprime la temperatura calculada 