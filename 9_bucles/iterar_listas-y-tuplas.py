# Iteración con for in:

lista_animales = ["Tigre", "Jaguar", "León", "Cocodrilo", "Lobo Marino"]

## Recorriendo la lista: lista_animales
for animal in lista_animales:
    print(animal)

lista_numeros = [5, 7, 15, 24, 25]

## Recorriendo la lista: lista_numeros
for numero in lista_numeros:
    print(numero * 2) # A cada número de la lista de números los multiplica * 2 y los imprime por consola

"""
¿Cómo podemos iterar 2 listas al mismo tiempo?
Eso se hace con un for dentro de otro for (for anidados)
Siempre y cuando ambas listas tengan la misma cantidad de elementos
Vamos a verlo con el siguiente ejemplo:
"""

lista_personas = ["Juan Martín Segovia", "Lucía Ventura", "Damián Rupérez"]
lista_libros = ["Cómic Amazing Spiderman #53", "Diario de Ana Frank", "Hamlet"]

for persona, libro in zip(lista_personas, lista_libros):
    print(f'Recorriendo lista_personas: {persona}')
    print(f'Recorriendo lista_libros: {libro}')
    
"Aclaramos que este método también se puede aplicar con más de 2 listas"


# Iteración con for in range:

for numero in range(5, 20):
    print(numero) # Imprime por consola números del 5 hasta el 19
    
print("\n")
    
for numero in range(5, 20+1):
    print(numero) # Imprime por consola números del 5 hasta el 20

print("\n")

for numero in range(10):
    print(numero) # Imprime por consola números del 0 hasta el 9
    
print("\n")
    
## Recorremos la lista de números por su índice:
    
    ### Pero NO es una forma óptima de recorrer una lista
for numero in range(len(lista_numeros)):
    print(lista_numeros[numero])

print("\n")

# Forma más correcta de recorrer una lista por sus índices:

for numero in enumerate(lista_numeros):
    #print(numero) # Devuelve una tupla (índice, valor)
    #print(numero[0]) # Devuelve el índice de la lista
    indice = numero[0]
    valor = numero[1]
    print(f'El índice es {indice} y su valor es: {valor}')


# Iteración con for/else:

for numero in lista_numeros:
    print(f'Ejecutando el último bucle, valor actual: {numero}')
else:
    print('La ejecución del bucle terminó')

"Todo lo anterior funciona exactamente igual para las tuplas"
