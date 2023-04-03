# Creando un conjunto con set:
conjunto_1 = set(["Dato1, Dato2"])

print(conjunto_1)

# Metiendo un conjunto de datos en otro conjunto:

conjunto_2 = frozenset(["dato1", "dato2"])
conjunto_3 = {conjunto_2, "dato3"}

print(conjunto_3)


# Teoría de conjuntos:

conjunto_4 = {1, 3, 5, 7}
conjunto_5 = {1, 3, 7}

## ¿Como podemos saber si un conjunto es subconjunto de otro conjunto?

resultado_conjuntos4y5 = conjunto_5.issubset(conjunto_4) # Esto se lee: conjunto_5 es un subconjunto de conjunto_4
### issubset() devuelve un dato booleano (True, False)

print(resultado_conjuntos4y5) # True en este caso

resultado_conjuntos4y5_invertido = conjunto_4.issubset(conjunto_5)

print(resultado_conjuntos4y5_invertido) # False en este caso, porque conjunto 4 tiene más datos que el conjunto 5

#### También hay otra forma de verificar esta solución:

resultado_conjuntos4y5_segundo_metodo = conjunto_5 <= conjunto_4
resultado_conjuntos4y5_segundo_metodo_invertido = conjunto_5 >= conjunto_4

print(resultado_conjuntos4y5_segundo_metodo) # True
print(resultado_conjuntos4y5_segundo_metodo_invertido) # False


## ¿Y como podemos saber si es un superconjunto?
"""
Recordar que hay que analizar las diferentes perspectivas.
Para los superconjuntos es al revés que los subconjuntos.
Y vamos a verlo con otros conjuntos de datos
"""

conjunto_6 = {2, 4, 6, 8, 9, 10}
conjunto_7 = {4, 6, 10}

resultado_conjuntos6y7 = conjunto_6.issuperset(conjunto_7)
resultado_conjuntos6y7_invertido = conjunto_7.issuperset(conjunto_6)

print(resultado_conjuntos6y7) # True
print(resultado_conjuntos6y7_invertido) # False

### El otro método:

resultado_conjuntos6y7_segundo_metodo = conjunto_6 > conjunto_7
resultado_conjuntos6y7_invertido_segundo_metodo = conjunto_7 > conjunto_6

print(resultado_conjuntos6y7_segundo_metodo) # True
print(resultado_conjuntos6y7_invertido_segundo_metodo) # False


## También podemos verificar si hay algún dato en común:
"""
Para esto usamos la función isdisjoint()
En el caso de que no encuentre algún valor en común entre 2 conjuntos,
devuelve True. Caso contrario, si encuentra al menos 1 valor en común, devuelve
False.
También podemos verlo con otros conjuntos
"""

conjunto_8 = {5, 20, 24, 47, 49, 56, 91, 96, 99}
conjunto_9 = {19, 40, 48, 50, 90, 94, 96, 100}
conjunto_10 = {1, 10, 40, 82, 86, 102, 120}

resultado_conjuntos8y9 = conjunto_9.isdisjoint(conjunto_8)
resultado_conjuntos8y10 = conjunto_10.isdisjoint(conjunto_8)

print(resultado_conjuntos8y9) # False
print(resultado_conjuntos8y10) # True



