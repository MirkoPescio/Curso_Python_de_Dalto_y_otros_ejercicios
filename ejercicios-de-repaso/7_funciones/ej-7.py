"""
Ejercicio 7
Escribir una función que reciba una muestra de números en una lista y devuelva
otra lista con sus cuadrados.
"""

# Mi solución:

def lista_inicial():
    lista_numeros_inicial = []
    nuevo_numero = ""
    ingreso = ""
    while(ingreso != "no"):
        nuevo_numero = float(input("Ingrese un número positivo: "))
        while(nuevo_numero < 0):
            nuevo_numero = float(input("Reingrese un número válido: "))
        lista_numeros_inicial.append(nuevo_numero)
        ingreso = input("¿Quiere seguir ingresando números? (si/no): ").lower()
    return lista_numeros_inicial

def calculo_cuadrados(lista_numeros):
    numeros = lista_numeros
    nueva_lista = []
    nuevo_numero = 0
    for numero in numeros:
        nuevo_numero = numero**2
        nueva_lista.append(nuevo_numero)
    return nueva_lista

def main():
    lista_inicial_numeros = lista_inicial()
    lista_numeros_al_cuadrado = calculo_cuadrados(lista_inicial_numeros)
    resultante = f'La lista actualizada es: {lista_numeros_al_cuadrado}'
    print(resultante)
main()


# Solución de la guía:

def square(sample):
    """Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

print(square([1, 2, 3, 4, 5]))