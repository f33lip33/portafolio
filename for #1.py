#Pide al usuario un número entero positivo y muestra su tabla de
#multiplicar del 1 al 10 usando un ciclo for.

numero = int(input("Ingrese un número entero positivo: "))

while numero <= 0:
    print("El número ingresado no es válido. Debe ser un entero positivo.")
    numero = int(input("Ingrese un número entero positivo: "))
    
int(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")