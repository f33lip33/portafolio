# 8 Pide al usuario un número entero y cuenta cuántos dígitos tiene usando un ciclo while.

n=int(input("Ingrese un numero entero : "))
c= 0
    
while n > 0:
    c=c + 1
    n= n //10
      
print(f"el numero tiene {c} digitos ")