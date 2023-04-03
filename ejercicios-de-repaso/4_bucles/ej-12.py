"""
Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
"""

# Mi solución:

palabra_o_frase = input("Ingrese una palabra o frase: ")
letra = input("Ingrese una letra: ")

while(len(letra) > 1):
    letra = input("Reingrese la LETRA: ")
    
contador_apariciones = 0

for caracter in palabra_o_frase:
    if(caracter == letra):
        contador_apariciones += 1

print("La letra " + letra + " aparece " + str(contador_apariciones) + " veces")


# Solución de la guía:

"""
frase = input("Introduce una frase: ")
letra = input("Introduce una letra")
contador = 0
for i in frase:
    if i == letra:
        contador += 1
print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, contador, frase))
"""

