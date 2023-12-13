numerador = int(input("introduce el numerador: "))
dividendo = int(input("introduce el dividendo: "))

while dividendo <= 0:
    print ("El dividendo debe ser mayor que cero. Introduzca un valor válido.")
    dividendo = int(input("introduce el dividendo: "))

conciente = numerador // dividendo
resto = numerador % dividendo

print( str(numerador)+ " entre " + str(dividendo) + " da un conciente " + str(conciente)+ " y un resto " + str(resto))