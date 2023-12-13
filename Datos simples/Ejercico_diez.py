def mueñeca(peso):
    cantidad=int(input("Introduce el numero de muñecas: "))
    peso= 75
    peso_muñeca = (peso*cantidad)/1000
    return peso_muñeca

def payaso(peso):
    cantidad=int(input("Introduce el numero de payasos: "))
    peso= 112
    peso_payaso = (peso*cantidad)/1000
    return peso_payaso 

def peso_paquete(mueñeca, payaso):
    peso_total = round (mueñeca + payaso,2)
    return peso_total

peso_mueñecas = mueñeca(0)
peso_payasos = payaso(0)
peso_total = peso_paquete(peso_mueñecas, peso_payasos)

print("El peso del paquete es " + str(peso_total) + "Kg")