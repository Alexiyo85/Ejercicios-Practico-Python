nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduce el precio del producto: "))  # Corregido aquí
numero_unidades = int(input("Introduce el número de unidades: "))
coste_total = numero_unidades * precio_producto
precio_formateado = "{:9.2f}€".format(precio_producto)
numero_formateado = "{:3d}".format(numero_unidades)  # Corregido aquí
coste_total_formateado = "{:11.2f}€".format(coste_total)  # Corregido aquí

print("El precio del producto es", precio_formateado, "y el número de unidades adquiridas es", numero_formateado, "por lo que hace un coste total de", coste_total_formateado)
