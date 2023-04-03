"""
Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última.
"""

# Mi solución:

palabra_o_texto = input("Ingrese una palabra o texto: ")
palabra_o_texto_invertido = palabra_o_texto[::-1]

for letra in palabra_o_texto_invertido:
    print(letra)


# Solución de la guía:

word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
