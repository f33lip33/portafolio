#Pide al usuario un número entero positivo y muestra todos los
#números impares del 1 hasta ese número usando un ciclo for.

numero = int(input("Ingrese un numero entero positivo: "))

while numero <= 0:
    print("El numero ingresado no es válido. Debe ser un entero positivo.")
    numero = int(input("Ingrese un numero entero positivo: "))

print(f"numeros impares hasta {numero}:")
for i in range(1, numero + 1, 2):
    print(i) 