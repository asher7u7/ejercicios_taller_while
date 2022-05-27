"""ejercicio 2 while:
Dado un rango de números enteros, obtener la
cantidad de números que contiene. Ej: para el rango
[5,6,7,8,9], la cantidad de números que contiene es 3
[6,7,8]"""

#input
inicio=int(input("ingrese el primer número del rango: "))
final=int(input("ingrese el ultimo número del rango: "))
variable=inicio
count2=0

#procesing

while variable<final-1:
    variable=variable+1
    count2=count2+1
    print(variable)

#output
print("dentro del rango ", str(inicio)," y ", str(final), " hay " ,str(count2), " números.")