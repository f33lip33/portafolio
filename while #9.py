# 9 Pide al usuario un número entero positivo y convierte ese número a binario usando un ciclo while.

entero = int(input("Ingrese un número entero positivo: "))

while entero < 0:
    print("el numero que ingreso no es positivo ")
    entero=int(input("Ingrese un numero positivo porfavor : "))
else:
    binario = ''

    while entero > 0:
        residuo = entero % 2
        binario = str(residuo) + binario
        entero //= 2
    
    print(f"El numero en binario es: {binario}")
