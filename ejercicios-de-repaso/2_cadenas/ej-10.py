"""
Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
"""

# Mi solución:

productos = input("Ingrese los productos que va a comprar (sepárelos con ','): ")
lista_productos = productos.split(",")

for producto in lista_productos:
    print(producto)
    


# Solución de la guía:

cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n')) #'\n es para dar un salto de línea en python'

