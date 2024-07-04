# 6 Pide al usuario un número entero positivo y muestra sus múltiplos del 1 al 10 usando un ciclo while.

numero=int(input("Ingrese un numero : "))
inicio= 1
 
while inicio <= 10:
    R= numero * inicio
    print(f"{numero}X{inicio}={R}")
    inicio += 1
print(" fin del programa")