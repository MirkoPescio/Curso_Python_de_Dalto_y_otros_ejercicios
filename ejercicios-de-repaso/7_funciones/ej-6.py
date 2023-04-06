"""
Ejercicio 6
Escribir una función que reciba una muestra de números en una lista y devuelva
su media. (Calcular el promedio en una suma de números)
"""

# Mi solución:

def suma_de_numeros(lista_numeros):
    sumatoria = sum([*lista_numeros])
    return sumatoria

def cantidad_de_numeros(lista_numeros):
    contador = 0
    for numero in lista_numeros:
        contador += 1
    return contador

def lista_de_numeros():
    numeros = []
    nuevo_numero = ""
    ingreso = ""
    while(ingreso != "no"):
        nuevo_numero = float(input("Ingrese un número positivo: "))
        while(nuevo_numero < 0):
            nuevo_numero = float(input("Reingrese un número válido: "))
        numeros.append(nuevo_numero)
        ingreso = input("¿Quiere seguir ingresando números? (si/no): ").lower()
    return numeros
        

def calculo_promedio():
    lista_numeros = lista_de_numeros()
    sumatoria = suma_de_numeros(lista_numeros)
    cantidad_numeros = cantidad_de_numeros(lista_numeros)
    promedio_o_media = sumatoria / cantidad_numeros
    return promedio_o_media
    
def main():
    resultante_promedio = calculo_promedio()
    respuesta = f'El promedio o media de la lista de números ingresada es {resultante_promedio}'
    print(respuesta)
main()

print("\n")

# Solución de la guía:

def mean(sample):
    """Función que calcula la media de una muestra de números.
    Parámetros
    sample: Es una lista de números
    Devuelve la media de los números en sample. 
    """
    return sum(sample)/len(sample)

print(mean([1, 2, 3, 4, 5]))
print(mean([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))




