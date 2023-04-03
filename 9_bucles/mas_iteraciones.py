
lista_juegos = ["Mad Max", "Resident Evil 4", "Uncharted 4", "The Last of Us", "FIFA 23"]

# Evitando que juegue Uncharted 4 con la sentencia continue:

for juego in lista_juegos:
    if juego == "Uncharted 4":
        continue
    print(f'Voy a jugar {juego}')
    
print("\n")

"""
Lo que hace la condición en el bucle anterior es:
En caso de que encuentre el juego 'Uncharted 4' en la lista, termina la vuelta del bucle
en ese punto y continua con el elemento que sigue. En otras palabras, no ejecuta el resto
del bloque pasando al juego que sigue en la lista
"""

# Terminar todo el bucle con la sentencia break:

for juego in lista_juegos:
    if juego == "The Last of Us":
        break
    print(f'Voy a jugar {juego}')
    
"""
A diferencia de la sentencia continue, break lo que hace es impedir que se ejecunten
los ciclos restantes de ese bucle
"""
    
print("\n")

cadena_1 = "Hola Mirko"

for caracter in cadena_1:
    print(caracter)
    
print("\n")
    
numeros = [2, 5, 8, 10]
# for en una sola línea de código:

numeros_duplicados = [x*2 for x in numeros]
numeros_al_cubo = [x**3 for x in numeros]

print(numeros_duplicados)
print(numeros_al_cubo)




