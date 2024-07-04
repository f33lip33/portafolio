#Pide al usuario que ingrese una cadena de texto y cuenta
#cuántas vocales hay en la cadena usando un ciclo for.

cadena = input("Ingrese una cadena de texto: ")


Cvocales = 0


vocales = ['a', 'e', 'i', 'o', 'u']


for caracter in cadena:
  
    if caracter in vocales:
        Cvocales += 1


print(f"La cantidad de vocales en el texto '{cadena}' es: {Cvocales}")