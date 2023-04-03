"""
Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es
un palíndromo.
"""

# Mi solución:

palabra = input("Ingrese una palabra: ")

if(palabra == palabra[::-1]):
    print(palabra + " es un palíndromo")
else:
    print(palabra + " no es un palíndromo")


# Solución de la guía:

word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

