valor = int(input("introduzca un valor: "))

while valor < 0:
    print("El valor no puede ser negativo, por favor introduzca otro valor.")
    valor = int(input("introduzca un valor: "))

suma = valor * (valor + 1) / 2
print("la suma de los primeros numeros enteros desde 1 hasta " + str(valor) + " es " + str(suma))