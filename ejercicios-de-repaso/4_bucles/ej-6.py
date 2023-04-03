"""
Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****
"""

# Mi solución:

num = int(input("Ingrese un numero entero: "))
cadena_triangulo = ""

for i in range(num):
    cadena_triangulo += "*"
    print(cadena_triangulo)


# Solución de la guía:

"""
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
    for j in range(i+1):
        print("*", end="")
    print("")
"""

