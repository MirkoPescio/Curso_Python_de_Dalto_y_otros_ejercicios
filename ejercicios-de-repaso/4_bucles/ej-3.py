"""
Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por comas.
"""

# Mi solución:

num = int(input("Ingrese un número entero positivo: "))

while (num <= 0):
    num = int(input("TE DIJE POSITIVO: "))
    
print("Te mostramos por consola los números impares desde el 1 hasta el " + str(num))

for i in range(1, num+1):
    if(i % 2 != 0):
        print(i)


# Solución de la guía:

"""
n = int(input("Introduce un número entero positivo: "))
for i in range(1, n+1, 2):
    print(i, end=", ")
"""

