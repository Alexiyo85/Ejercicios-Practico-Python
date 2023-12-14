renta=int(input("Inserta la renta anual: "))

if renta < 10000:
    print ("Su tipo impositivo es de 5%")
    tipo= 5/100
elif (renta >=10000) and (renta <20000):
    print ("Su tipo impositivo es de 15%")
    tipo= 15/100
elif (renta >=20000) and (renta <35000):
    print ("Su tipo impositivo es de 20%")
    tipo= 20
elif (renta >=35000) and (renta <60000):
    print ("Su tipo impositivo es de 30%")
    tipo= 30
elif (renta >=60000):
    print ("Su tipo impositivo es de 45%")
    tipo=45
print("Tienes que pagar", renta*tipo, "€")
