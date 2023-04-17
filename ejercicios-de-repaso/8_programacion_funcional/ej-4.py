"""
Ejercicio 4
Escribir una función que reciba otra función booleana y una lista, y devuelva otra 
lista con los elementos de la lista que devuelvan True al aplicarles la función 
booleana.
"""

# Mi solución:

def es_par(numero):
    valor_booleano = False
    if (numero % 2 == 0):
        valor_booleano = True
    return valor_booleano

def lista_de_numeros():
    lista_numeros = []
    numero = ""
    cantidad_de_numeros = int(input("Ingrese la cantidad de números que va a ingresar a la lista: "))
    while(cantidad_de_numeros <= 0):
        cantidad_de_numeros = int(input("Reingrese la cantidad de números que va a ingresar a la lista: "))
    for num in range(1, cantidad_de_numeros+1):
        numero = float(input(f"Ingrese el número n°{num}: "))
        lista_numeros.append(numero)
    return lista_numeros

def main():
    todos_los_numeros = lista_de_numeros()
    lista_numeros_pares = []
    for numero in todos_los_numeros:
        if(es_par(numero)):
            lista_numeros_pares.append(numero)
    print("Lista de números pares:")
    print(lista_numeros_pares)
main()

# Solución de la guía:

def filtra_lista(funcion, lista):
    '''Función que filtra los elementos de una lista que devuelven true al aplicarle una función booleana.

    Parámetros:
        - funcion: Es una función booleana (devuleve true o false)
        - lista: Es una lista con valores que se pasarán como argumentos a funcion.
    Devuelve:
        Una lista con los elementos de la lista que devuelven true al aplicarles la función booleana.
    '''
    l = []
    for i in lista:
        if funcion(i):
            l.append(i)
    return l

def par(n):
    return n % 2 == 0

print(filtra_lista(par, [1, 2, 3, 4, 5, 6]))

