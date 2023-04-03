"""
Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos 
decimales y muestre por pantalla el número de euros y el número de céntimos del precio 
introducido.
"""

# Mi solución:

nombre_producto = input("Ingrese el nombre del producto: ")

while len(nombre_producto) <= 5:
    nombre_producto = input("Ingrese un nombre más descriptivo para el producto: ")

precio_producto = float(input("Ingrese el precio unitario del producto: "))

while precio_producto <= 0:
    precio_producto = float(input("ingrese un número válido para el precio del producto: "))

precio_unitario_producto = round(precio_producto, 2)
precio_array = str(precio_unitario_producto).split(".")
print(precio_array)
euros = precio_array[0]
centimos = precio_array[1]

respuesta = "El precio unitario del producto " + nombre_producto + " es de €" + euros + " con ." + centimos + " céntimos"
print(respuesta)


# Solución de la guía:

precio = input("Introduce el precio del producto con dos decimales:  ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'céntimos.')
