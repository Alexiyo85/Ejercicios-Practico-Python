fecha_nacimiento=input("Introduce la fecha de nacimiento con el siguiente formato (dd/mm/aaaa): ")

if len(fecha_nacimiento) == 8:
    print("Dia", fecha_nacimiento[:1])
    print ("Mes", fecha_nacimiento[2:3])
    print("Año", fecha_nacimiento[-4:])
elif len(fecha_nacimiento) ==10:
    print("Dia", fecha_nacimiento[:2])
    print ("Mes", fecha_nacimiento[3:5])
    print("Año", fecha_nacimiento[-4:])
else:
    print("Introduzca el formato correcto ")