"""
Ejercicio 11
Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades 
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 
6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 
dígitos enteros y 2 decimales.
"""

# Mi solución:

nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
cantidad_unidades = int(input("Ingrese la cantidad de unidades del producto: "))
precio_unitario_redondeado = round(precio_unitario, 2)

respuesta = "El producto " + nombre_producto + " tiene un valor de $" + str(precio_unitario_redondeado) + " por unidad y la cantidad elegida para la compra es de " + str(cantidad_unidades) + " unidades"
print(respuesta)
precio_total = cantidad_unidades * precio_unitario_redondeado
respuesta_precio_final = "El monto total a pagar por " + str(cantidad_unidades) + " unidades de " + nombre_producto + " es de $" + str(round(precio_total, 2))
print(respuesta_precio_final)


# Solución de la guía:

"""
producto = input('Introduce el nombre del producto: ')
precio = float(input('Introducde el precio unitario: '))
unidades = int(input('Introduce el número de unidades: '))
print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))
"""

