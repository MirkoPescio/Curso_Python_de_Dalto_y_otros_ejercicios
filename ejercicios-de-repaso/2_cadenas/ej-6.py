"""
Ejercicio 6
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""

# Mi solución:

texto = input("Ingrese un texto: ")
vocal = input("Ingrese una vocal: ")

vocales = "aeiou"

while vocales.find(vocal) == -1:
    vocal = input("Ingrese una VOCAL (a,e,i,o,u): ")

nuevo_texto = texto.replace(vocal, vocal.upper())
print(nuevo_texto)


# Solución de la guía:

"""
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))
"""

