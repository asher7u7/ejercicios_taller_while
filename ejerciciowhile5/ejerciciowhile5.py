"""Ejercicio 5
Dado un número determinar cuántos dígitos tiene."""

#input

n=int(input("digite un número: "))
contador=0

#procesing

while n>0:
    n=n//10
    contador=contador+1


#output
print("el número tiene ",contador," digitos.")