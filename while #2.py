# 2 Pide al usuario un número entero positivo y muestra todos los números del 1 hasta ese número usando un ciclo while.

N=int(input("Ingrese el numero : "))
contador=1
    
while N <= 0:
    
    print(f"El numero {N} no es positivo")
    N=int(input("ingrese un numero que si sea positivo : "))
    
while contador <= N:
    print(contador)
    contador= contador + 1
    
print("fin ")