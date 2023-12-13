try:
    peso = float(input("introduzca su peso en Kg: "))
    altura = float(input("introduzca su altura en cm: "))
    
    if altura == 0:
        print("La altura no puede ser 0. Intente de nuevo.")
    else:
        imc = round(peso / (altura / 100) ** 2, 2 )  #round --> redondea a los decimales que se necesiten.
        print("Tu índice de masa corporal es ", str(imc))
        
except ValueError:
    print("Error: por favor ingrese números válidos para el peso y la altura.")