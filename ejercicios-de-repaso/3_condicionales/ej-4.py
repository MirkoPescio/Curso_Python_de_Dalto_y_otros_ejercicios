"""
Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es par o impar.
"""

# Mi solución:

num = int(input("Ingrese un número entero: "))

es_par_impar = num % 2

if (es_par_impar == 0):
    print(str(num) + " es par")
else:
    print(str(num) + " es impar")


# Solución de la guía:

"""
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
    print("El número " + str(n) + " es par")
else:
    print("El número " + str(n) + " es impar")
"""

