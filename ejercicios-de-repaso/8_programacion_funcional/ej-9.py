"""
Ejercicio 9
Escribir una función que calcule el módulo de un vector.
"""

# Mi solución:


def lista_de_coordenadas(dimensiones):
    lista = []
    for i in range(1, dimensiones+1):
        i = float(input(f"Ingrese el valor de la coordenada n°{i}: "))
        lista.append(i)
    return lista

def calcular_modulo(lista_de_coordenadas):
    acumulador = 0
    for coordenada in lista_de_coordenadas:
        acumulador += coordenada**2
    calculo = (acumulador) ** (1/2)
    return calculo

def main():
    dimensiones = int(input("Ingrese el espacio vectorial (dimensiones) del vector: "))
    while(dimensiones <= 0):
        dimensiones = int(input("Reingrese el espacio vectorial (dimensiones) del vector: "))
    vector_lista = lista_de_coordenadas(dimensiones)
    modulo_vector_lista = calcular_modulo(vector_lista)
    rta_modulo = f'El módulo del vector lista {vector_lista} es igual a {modulo_vector_lista} u{dimensiones}'
    print(rta_modulo)
main()

print("\n")

# Solución de la guía:

## Solución 1:

def sum_square(x, y):
    '''
    Función que recibe dos valores y calcula la suma del primero más el cuadrado del segundo.
    Parámetros:
        x: Es un número real.
        y: Es un número real.
    Devuelve:
        x + y²
    '''
    return x + y ** 2

def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    from functools import reduce
    return reduce(sum_square, v, 0) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))
print("\n")

## Solución 2:

def module(v):
    '''
    Función que calcula el módulo de un vector.
    Parámetros:
        v: Una tupla de números reales.
    Devuelve:
        El módulo del vector v.
    '''
    return sum([x ** 2 for x in v]) ** 0.5

print(module((3, 4)))
print(module((1, 2, 3)))

