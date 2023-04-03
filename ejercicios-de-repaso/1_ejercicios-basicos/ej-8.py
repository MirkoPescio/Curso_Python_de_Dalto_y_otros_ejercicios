"""
Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla
la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
y <c> y <r> son el cociente y el resto de la división entera respectivamente.
"""

# Mi solución:

n = int(input("Ingrese un número entero: "))
m = int(input("Ingrese otro número entero: "))
c = n / m
r = n % m
print("El cociente de la división entre " + str(n) + " y " + str(m) + " es igual a: " + str(c))
print("El cociente de la división entre " + str(n) + " y " + str(m) + " es de: " + str(r))

# Solución de la página web:

"""
n = input("Introduce el dividendo (entero): ")
m = input("Introduce el divisor (entero): ")
print(n + " entre " +  m + " da un cociente " + str(int(n) // int(m)) + " y un resto " + str(int(n) % int(m)))
"""

