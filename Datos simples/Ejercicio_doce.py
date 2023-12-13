precio = 3.49
descuento_barra = 60/100
cantidad= int(input("Barra de pan que no son del dia: "))
descuento_por_barra_ayer= round(precio - (precio*descuento_barra),2)
precio_por_barra_ayer= round(precio*descuento_barra,2)
total = round(precio_por_barra_ayer* cantidad,2)
print ("El descuento por una barra de pan que no es fresca es: " + str(descuento_barra)+"%")
print ("El precio sin descuento es : " + str(precio) +"€")
print("El precio con descuento es: " +str(precio_por_barra_ayer) + "€")
print("El descuento por no se fresca es: " + str(descuento_por_barra_ayer) + "€")
print("El coste total de " + str(cantidad) + " barra/s es " + str(total) + "€")

