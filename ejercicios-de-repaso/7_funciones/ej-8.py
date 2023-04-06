"""
Ejercicio 8
Escribir una función que reciba una muestra de números en una lista y devuelva un
diccionario con su media, varianza y desviación típica.
"""

# Mi solución:

def lista_de_numeros():
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

def media(lista_numeros):
    sumatoria = sum([*lista_numeros])
    cantidad_de_numeros = len([*lista_numeros])
    calculo_media = sumatoria / cantidad_de_numeros
    return calculo_media

def varianza(lista_numeros):
    sumatoria_cuadrados = sum(calculo_cuadrados([*lista_numeros]))
    cantidad_de_numeros = len([*lista_numeros])
    promedio = media(lista_numeros)
    calculo_varianza = (sumatoria_cuadrados/cantidad_de_numeros) - promedio**2
    return calculo_varianza

def desviacion_tipica(lista_numeros):
    variacion = varianza(lista_numeros)
    calculo_desviacion_tipica = variacion ** 0.5
    return calculo_desviacion_tipica

def main():
    lista_inicial = lista_de_numeros()
    media_resultado = media(lista_inicial)
    varianza_resultado = varianza(lista_inicial)
    desviacion_tipica_resultado = desviacion_tipica(lista_inicial)
    diccionario_resultante = {}
    diccionario_resultante["media"] = media_resultado
    diccionario_resultante["varianza"] = varianza_resultado
    diccionario_resultante["desviación típica"] = desviacion_tipica_resultado
    print(diccionario_resultante)
main()

print("\n")

# Solución de la guía:

def square(sample):
    """
    Función que calcula los cuadrados de una lista de números.
    Parámetros
    sample: Es una lista de números
    Devuelve una lista con los cuadrados de los números de la lista sample.
    """
    list = []
    for i in sample:
        list.append(i**2)
    return list

def statistics(sample):
    """Función que calcula la media, varianza y desviación típica de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve un diccionario con la media, varianza y desviación típica de los números en sample.
    """
    stat = {}
    stat['media'] = sum(sample)/len(sample)
    stat['varianza'] = sum(square(sample))/len(sample)-stat['media']**2
    stat['desviacion tipica'] = stat['varianza']**0.5
    return stat

print(statistics([1, 2, 3, 4, 5]))
print(statistics([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))

