inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
bonificacion=2400
puntos = float(input("Introduce la puntuacion del trabajador: "))
if puntos < 0.4:
    print ("Inaceptable")
    print ("tu bonificacion es la siguiente", bonificacion*puntos, "€")
elif (puntos >0.4) and (puntos < 0.6):
    print("Aceptable")
    print ("tu bonificacion es la siguiente", bonificacion*puntos, "€")
elif puntos >= 0.6:
    print("meritorio")
    print ("tu bonificacion es la siguiente", bonificacion*puntos, "€")

