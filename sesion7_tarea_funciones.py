import math  # Se importa para usar el valor de PI

# Función para calcular el área de un triángulo
# Valores de entrada: base, altura
# Retorna: área del triángulo
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


# Función para calcular el área de un círculo
# Valor de entrada: radio
# Retorna: área del círculo
def area_circulo(radio):
    area = math.pi * radio ** 2
    return area


