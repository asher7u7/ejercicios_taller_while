"""ejercicio 3 while:
Dado un rango de números enteros obtener la
cantidad de números pares que contiene."""

#input
inicio=int(input("ingrese el primer número del rango: "))
final=int(input("ingrese el ultimo número del rango: "))
variable=inicio
count2=0
count3=0
#procesing

while variable<final-1:
    variable=variable+1
    count2=count2+1
    if variable%2==0:
        print(variable)
        count3=count3+1


#output
print("dentro del rango ", str(inicio)," y ", str(final), " hay " ,str(count2), " números enteros y ",str(count3)," números pares.")