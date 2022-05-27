"""ejercicio 1 del while
Calcular la suma de los N primeros números
naturales."""

#input
n=int(input("ingrese el valor de n: "))
vez=0
resul=0

#procesing
while vez<n:
    vez=vez+1
    resul=vez+resul


#output
print("el resultado es ",resul)