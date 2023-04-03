"""
Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
"""

# Mi solución:

texto = input("Ingrese una palabra o un texto: ")

for i in range(1, 10+1):
    print(texto)


# Solución de la guía:

word = input("Introduce una palabra: ")
for u in range(10):
    print(word)

