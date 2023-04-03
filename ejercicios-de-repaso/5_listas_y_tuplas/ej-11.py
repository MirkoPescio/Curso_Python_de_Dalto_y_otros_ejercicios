"""
Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas
y muestre por pantalla su producto escalar.
"""

# Mi solución:

vector_1 = (1, 2, 3)
vector_2 = (-1, 0, 2)

vector_lista_1 = []
vector_lista_2 = []

for escalares in vector_1:
    vector_lista_1.append(escalares)

for escalares in vector_2:
    vector_lista_2.append(escalares)

print(vector_lista_1)
print(vector_lista_2)

producto_escalar = 0

for i in range(len(vector_lista_1)):
    producto_escalar += vector_lista_1[i] * vector_lista_2[i]

print("El producto escalar entre ambos vectores es igual a " + str(producto_escalar))

# Solución de la guía:

"""
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
    product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product)) 
"""

