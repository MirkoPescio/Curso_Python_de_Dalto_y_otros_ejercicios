"""
Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal.
"""

# Mi solución:

string = input("Ingrese una palabra o texto: ")
lista_string = list(string)
vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
    count = 0
    for caracter in lista_string:
        if(vocal == caracter):
            count += 1
    print("La vocal '" + vocal + "' aparece " + str(count) + " vez/veces")


# Solución de la guía:

"""
word = input("Introduce una palabra: ")
vocals = ['a', 'e', 'i', 'o', 'u']
for vocal in vocals: 
    times = 0
    for letter in word: 
        if letter == vocal:
            times += 1
    print("La vocal " + vocal + " aparece " + str(times) + " veces")
"""

