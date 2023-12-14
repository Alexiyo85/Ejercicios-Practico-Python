nombre = input("Introduce tu nombre: ")
sexo = input("Introduce tu sexo (M=mujer, H=hombre): ")

nombre_minusculas = nombre.lower()

if sexo.lower() == "h":
    if nombre_minusculas < "m":
        grupo = "B"
    else:
        grupo = "A"
elif sexo.lower() == "m":
    if nombre_minusculas < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    grupo = "No especificado"

print("Tu grupo es", grupo)
