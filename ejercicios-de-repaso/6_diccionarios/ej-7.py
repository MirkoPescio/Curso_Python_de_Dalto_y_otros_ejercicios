"""
Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra.
El programa debe preguntar el artículo y su precio y añadir el par al diccionario,
hasta que el usuario decida terminar.
Después se debe mostrar por pantalla la lista de la compra y el coste total,
con el siguiente formato

Lista de la compra
Artículo 1     Precio
Artículo 2     Precio
Artículo 3     Precio
    …            …
  Total         Coste
"""

# Mi solución:

cesta_de_compra = {}
contador = 1

articulo = input("Ingrese el nombre de un producto: ")
precio = float(input("Ingrese el precio del producto: "))
ingreso = ""

while(precio <= 0):
    precio = float(input("Reingrese el precio: "))

cesta_de_compra["producto " + str(contador)] = (articulo, precio)

while(ingreso.capitalize() != "No"):
    ingreso = input("¿Quiere seguir ingresando productos? (si/no): ")
    if(ingreso.capitalize() == "No"):
        break
    print("Nuevo producto a añadir:")
    contador += 1
    articulo = input("Ingrese el nombre de un producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    while(precio <= 0):
        precio = float(input("Ingrese el precio del producto: "))
    cesta_de_compra["producto " + str(contador)] = (articulo, precio)

print("\n" + "Lista de la compra:")
print(cesta_de_compra)

precio_total = 0

for clave, tupla in cesta_de_compra.items():
    precio_total += tupla[1]
    
print("Precio total: " + str(precio_total))


# Solución de la guía:

"""
cesta = {}
continuar = True
while continuar:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item] = precio
    continuar = input('¿Quieres añadir artículos a la lista (Si/No)? ') == "Si"
coste = 0
print('Lista de la compra')
for item, precio in cesta.items():
    print(item, '\t', precio)
    coste += precio
print('Coste total: ', coste)
"""

