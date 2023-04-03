"""
Ejercicio 12
Escribir un programa que almacene las matrices:


 A = ((1, 2, 3), (4, 5, 6))
 B = ((-1, 0), (0, 1), (1, 1))

en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas,
representando cada vector fila en una lista.
"""

# Mi solución:

A = ((1, 2, 3), (4, 5, 6))
B = ((-1, 0), (0, 1), (1, 1))

vector_lista_A = []
vector_lista_B = []

for vector_A in A:
    vector_lista_A.append(vector_A)

for vector_B in B:
    vector_lista_B.append(vector_B)

producto_escalar_A = 0
producto_escalar_B = 0

print(vector_lista_A)
print(vector_lista_B)

for vector in vector_lista_A:
    for escalar in range(len(vector)):
        producto_escalar_A += vector_lista_A[0][escalar] * vector_lista_A[1][escalar]

for vector in vector_lista_B:
    for escalar in range(len(vector)):
        producto_escalar_B += vector_lista_B[0][escalar] * vector_lista_B[1][escalar] * vector_lista_B[2][escalar]

print("Producto escalar entre los vectores de la matriz A: " + str(producto_escalar_A))
print("Producto escalar entre los vectores de la matriz B: " + str(producto_escalar_B))


# Solución de la guía:

a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
result = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])
