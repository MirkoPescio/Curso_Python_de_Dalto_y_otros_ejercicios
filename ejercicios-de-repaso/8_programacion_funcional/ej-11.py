"""
Ejercicio 11
Escribir una función que reciba una muestra de números y devuelva los valores 
atípicos, es decir, los valores cuya puntuación típica sea mayor que 3 o menor 
que -3. Nota: La puntuación típica de un valor se obtiene restando la media y 
dividiendo por la desviación típica de la muestra.
"""

from statistics import mean, stdev

# puntuacion_tipica = (puntuacion_directa - promedio) / desviacion_estandar

# Mi solución:

def cantidad_de_numeros_a_registrar():
    cantidad_de_numeros = int(input("Ingrese la cantidad de números a registrar: "))
    while(cantidad_de_numeros <= 0):
        cantidad_de_numeros = int(input("Reingrese la cantidad de números a registrar: "))
    return cantidad_de_numeros

def lista_de_numeros(cantidad_de_numeros):
    lista_numeros = []
    for i in range(1, cantidad_de_numeros+1):
        i = int(input(f"Ingrese el número n°{i}: "))
        lista_numeros.append(i)
    return lista_numeros

def calculos(muestra_de_numeros): # La muestra es la lista de números
    valores_atipicos = []
    puntuacion_directa = ""
    promedio = mean(muestra_de_numeros)
    desviacion_estandar = stdev(muestra_de_numeros)
    for numero in muestra_de_numeros:
        puntuacion_directa = numero
        puntuacion_tipica = (puntuacion_directa - promedio) / desviacion_estandar
        if((puntuacion_tipica < -3) or (puntuacion_tipica > 3)):
            valores_atipicos.append(numero)
    return valores_atipicos

def main():
    cantidad_de_numeros = cantidad_de_numeros_a_registrar()
    lista_numeros = lista_de_numeros(cantidad_de_numeros)
    lista_valores_atipicos = calculos(lista_numeros)
    print("LA LISTA FILTRADA DE NUMEROS ATIPICOS ES:")
    print(lista_valores_atipicos)
main()

# Solución de la guía:

def atipico(muestra):
    media = mean(muestra)
    desviacion = stdev(muestra)
    def f(n):
        puntuacion = (n - media) / desviacion
        return (puntuacion < -3) or (puntuacion > 3)
    return f

def datos_atipicos(muestra):
    return list(filter(atipico(muestra), muestra))

print(datos_atipicos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1000]))
