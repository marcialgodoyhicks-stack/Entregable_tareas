# Se crea una variable para ingresar la cantidad de empleados
cantidad_empleados = int(input("Ingrese la cantidad de empleados: ")) 

#Se utiliza un bucle for para reptir la ejecución el codigo  en rango determinado de veces. 
# Ademas se crea una variable de tipo contador
for contador in range(0, cantidad_empleados):
    sueldo_bruto = float(input(f"Ingrese el sueldo bruto del empleado: {contador + 1}: $")) #Acá se crea un input para ingresar el sueldo 
   # y se aplica al contador + 1 para que lo realice a en función de los empleados que declaramos anteriormente. 
    
        # Inicializamos el bono
    bono = 0

    if sueldo_bruto < 600000: #se utilizan condicionantes para establecer el bono. 
        bono = 20000 #se crea la variable bono
    elif 600000 <= sueldo_bruto <= 900000:
        bono = 30000
    else:
        bono = 50000

    sueldo_bruto_final = sueldo_bruto + bono #Se crea la variable de calculo final de sueldo bruto. 
    
    descuento_impuestos = sueldo_bruto * 0.215 # Se aplica el descuento de impuestos con cálculo 
    sueldo_liquido_final = sueldo_bruto_final - descuento_impuestos  # Y se cálcula el sueldo liquido final.  
    
    #Se imprimen los bonos aplicados, el total de sueldo bruto antes de impuestos y el sueldo liquido.  
    print(f"Bono aplicado: ${bono}")
    print(f"Sueldo bruto más bono: ${sueldo_bruto_final}")
    print(f"Sueldo líquido final (Menos descuentos): ${sueldo_liquido_final}")
