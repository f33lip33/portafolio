# 4 Pide al usuario un número entero y suma sus dígitos usando un ciclo while

N=int(input("Ingrese un numero : "))
suma= 0

while N != 0:
    digito = N % 10
    suma += digito
    N = N//10
print(f"La suma de los digitos es : {suma}")