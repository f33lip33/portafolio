# 5 Escribe un programa que elija un número aleatorio entre 1 y 10 y
#permita al usuario adivinarlo, dándole pistas de "mayor" o "menor" hasta que acierte. Usa un ciclo while.

import random

random_num = random.randint(1, 10)

print("Adivina el número entre 1 y 10")

numero= int(input("Ingresa tu numero: "))

while numero != random_num:
    
    if numero < random_num:
        print("¡El número es mayor!")
        
    else:  
        print("¡El número es menor!")
    
    numero= int(input("Inténtalo de nuevo: "))

print(f"Adivinaste el número {random_num}.")