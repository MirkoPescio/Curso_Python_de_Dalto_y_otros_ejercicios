"""
Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por comas,
los guarde en una lista y muestre por pantalla su media y desviación típica.
"""

# Mi solución:

lista_muestra_de_numeros = [54, 98, 24, 25, 2]

## Cálculo de media:

suma_media = 0

for numero in lista_muestra_de_numeros:
    suma_media += numero
    
media = suma_media / len(lista_muestra_de_numeros)

print("La media de los números de la lista es igual a " + str(media))

## Cálculo de desviación típica:

acumulacion = 0

for numero in lista_muestra_de_numeros:
    acumulacion += (numero - media)**2
    
desviacion_tipica = (acumulacion / len(lista_muestra_de_numeros)) ** (1/2)

print("La desviación típica de los números de la lista es igual a " + str(desviacion_tipica))


# Solución de la guía:

"""
sample = input("Introduce una muestra de números separados por comas: ")
sample = sample.split(',')
n = len(sample)
for i in range(n):
    sample[i] = int(sample[i])
sample = tuple(sample)
sum = 0
sumsq = 0
for i in sample:
    sum += i
    sumsq += i**2
mean = sum/n
stdev = (sumsq/n-mean**2)**(1/2)
print('La media es', mean, ', y la desviación típica es', stdev)
"""

