# 7 Pide al usuario que ingrese un número positivo. Si el usuario ingresa un
#número negativo, solicita nuevamente la entrada hasta que ingrese un número positivo. Usa un ciclo while.

numero=int(input("Ingrese un numero positivo = "))

while numero < 0:
    print("el numero que ingreso no es positivo ")
    numero=int(input("Ingrese un numero positivo= "))
    
    if numero > 0:
        print(f"el Numero {numero} si es positivo")

