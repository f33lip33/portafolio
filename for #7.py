#Pide al usuario un número entero positivo y determina si
#es primo usando un ciclo for.

N = int(input("Ingrese un número entero positivo: "))

while N <= 1:
    print("El número ingresado no es válido. Debe ser un entero positivo mayor que 1.")
    N = int(input("Ingrese un número entero positivo: "))

primo = True

for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        primo = False
        break

if primo:
    print(f"{N} es un número primo.")
else:
    print(f"{N} no es un número primo.")