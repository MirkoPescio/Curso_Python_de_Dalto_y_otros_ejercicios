"""
Ejercicio 3
Escribir una función que reciba otra función y una lista, y devuelva otra lista con 
el resultado de aplicar la función dada a cada uno de los elementos de la lista.
"""

# Mi solución:


def ordenar_lista_ascendente(lista):
    lista.sort()
    return lista

def ordenar_lista_descendente(lista):
    lista.sort(reverse=True)
    return lista

def main():
    lista = []
    cantidad_de_numeros = int(input("Ingrese la cantidad de números a ingresar en la lista: "))
    while(cantidad_de_numeros <= 0 or cantidad_de_numeros > 100):
        cantidad_de_numeros = int(input("Reingrese la cantidad de números a ingresar en la lista: "))
    num = ""
    for i in range(1, cantidad_de_numeros+1):
        num = float(input(f"Ingrese el valor n°{i}: "))
        lista.append(num)
    lista_1 = ordenar_lista_ascendente(lista)
    print(lista_1)
    lista_2 = ordenar_lista_descendente(lista)
    print(lista_2)
main()

# Solución de la guía:

def aplica_funcion_lista(funcion, lista):
    '''Función que aplica una función a todos los elementos de una lista.

    Parámetros:
        funcion: Es una función.
        lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con el resultado de aplicar la función a los valores de la lista.
    '''
    l = []
    for i in lista:
        l.append(funcion(i))
    return l

def cuadrado(n):
    return n * n

print(aplica_funcion_lista(cuadrado, [1, 2, 3, 4]))

