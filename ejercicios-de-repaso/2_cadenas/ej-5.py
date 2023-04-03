"""
Ejercicio 5
Escribir un programa que pida al usuario que introduzca una frase en la consola y 
muestre por pantalla la frase invertida.
"""

# Mi solución:

texto = input("Ingrese un texto: ")
texto_invertido = texto[::-1]
print(texto_invertido)


# Solución de la guía:

frase = input("Introduce una frase: ")
print(frase[::-1])
