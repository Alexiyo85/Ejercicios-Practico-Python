nombre = input("Introduce el nombre: ")
primer_apellido = input("Introduce el primer apellido: ")
segundo_apellido = input("Introduce el segundo apellido: ")

nombre_completo = nombre + " " + primer_apellido + " " + segundo_apellido

print(nombre_completo.upper()) # Todas las letras en mayúsculas
print(nombre_completo.lower()) # Todas las letras en minúsculas
print(nombre_completo.title()) # La primera letra de cada palabra en mayúsculas y el resto en minúsculas