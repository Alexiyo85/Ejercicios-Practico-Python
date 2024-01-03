edad = int(input("introduce la edad"))

if edad < 4: 
    print("el precio de la entrada es gratis")
elif (edad >= 4) and (edad < 18):
    print ("tienes que pagar 5€") 
elif edad >=18 :
    print ("tienes que pagar 10€")