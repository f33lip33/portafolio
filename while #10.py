# 10 Escribe un programa que simule un cajero automático. Pide
# al usuario que ingrese su PIN y permite tres intentos para ingresarlo correctamente. Si no lo
# hace en tres intentos, muestra un mensaje de bloqueo. Usa un ciclo while.

pin=(1234)
intentos = 3 
contador = 1

c=int(input("Ingrese su pin: "))

while c != pin:
  if contador < intentos:
    print("la contraseña es incorrecta")
    c=int(input("Ingrese numavente su contraseña: "))
    contador += 1
    
  else:
        print("Ha excedido el número máximo de intentos")
        break

if c == pin:
    print("la contraseña que ingresaste es correcta")