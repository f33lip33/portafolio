#Pide al usuario un número entero positivo NNN y
#suma los primeros NNN números naturales usando un ciclo for.

N = int(input("Ingrese un número entero positivo: "))

while N <= 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
    N = int(input("Ingrese un número entero positivo: "))

suma = 0

for i in range(1, N + 1):
    suma += i

print(f"La suma de los primeros {N} números naturales es: {suma}")