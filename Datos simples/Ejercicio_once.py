interes= float(4/100)
primer_año= float(input("Introducir cantidad: "))
respuesta = input("Desea introducir otra cantidad 'Si/No'")
while respuesta != "No":
    primer_año= float(input("Introducir cantidad: "))
    primer_año += primer_año 
    respuesta = input("Desea introducir otra cantidad: ")

segundo_año= float(input("Introducir cantidad: "))
respuesta = input("Desea introducir otra cantidad 'Si/No'")
while respuesta != "No":
    segundo_año= float(input("Introducir cantidad: "))
    segundo_año += primer_año 
    respuesta = input("Desea introducir otra cantidad: ")

tercer_año= float(input("Introducir cantidad: "))
while respuesta != "No":
    tercer_año= float(input("Introducir cantidad: "))
    tercer_año += primer_año 
    respuesta = input("Desea introducir otra cantidad: ")

print("Cantidad Ingresada el primer año: " + str(primer_año))
print( "Rendimiento obtenido el primer año: " + str(primer_año*interes))
print("Total obtenido al final del primer año: " + str(primer_año+(primer_año*interes)))

print("Cantidad Ingresada el segundo año: " + str(segundo_año))
print( "Rendimiento obtenido el segundo año: " + str(segundo_año*interes))
print("Total obtenido al final del segundo año: " + str(segundo_año+(segundo_año*interes)))

print("Cantidad Ingresada el tercer año: " + str(tercer_año))
print( "Rendimiento obtenido el tercer año: " + str(tercer_año*interes))
print("Total obtenido al final del tercer año: " + str(tercer_año+(tercer_año*interes)))

print("Monto total obtenido a lo largo de los tres años: " + str(primer_año+(primer_año*interes) + segundo_año+(segundo_año*interes) + tercer_año+(tercer_año*interes)))
