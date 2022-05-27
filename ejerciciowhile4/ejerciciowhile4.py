"""ejercicio 4 while:
Obtener la cantidad de los primeros N números
múltiplos de 5."""


#input
n=int(input("ingrese el valor de n: "))
vez=0
resul=0

#procesing
while vez<n:
    vez=vez+1
    resul=vez*5
    print(resul)

#output
print("el resultado es ",resul)