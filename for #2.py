#Escribe un programa que sume todos los números pares
#del 1 al 100 usando un ciclo for.

Npares = 0
for num in range(1, 101):
     if num % 2 == 0:
         Npares += num
         
print(f"La suma de todos los números pares del 1 al 100 es: {Npares}")