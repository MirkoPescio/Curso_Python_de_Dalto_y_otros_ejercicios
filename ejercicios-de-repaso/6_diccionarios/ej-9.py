"""
Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura
será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura,
pagar una existente o terminar. Si desea añadir una nueva factura se preguntará
por el número de factura y su coste y se añadirá al diccionario.
Si se desea pagar una factura se preguntará por el número de factura y se eliminará
del diccionario. Después de cada operación el programa debe mostrar por pantalla
la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

# Mi solución:

dicc_facturas = {}
total_pagado = 0
total_pendiente = 0
ingreso_factura = int(input("Ingrese el número de factura a pagar: "))
registro = ""
numero_factura = ""

while(ingreso_factura < 0):
    ingreso_factura = int(input("Reingrese el número de factura a pagar: "))
    
precio_factura = float(input("Ingrese el monto de la factura " + str(ingreso_factura) + ": "))

while(precio_factura <= 0):
    precio_factura = float(input("Reingrese el monto de la factura " + str(ingreso_factura) + ": "))

dicc_facturas[ingreso_factura] = precio_factura

while(registro.capitalize() != "No"):
    registro = input("¿Quiere seguir registrando facturas? (si/no): ")
    if(registro.capitalize() == "No"):
        break
    print("Nuevo registro:")
    ingreso_factura = int(input("Ingrese el número de factura a pagar: "))
    while(ingreso_factura < 0):
        ingreso_factura = int(input("Reingrese el número de factura a pagar: "))
    precio_factura = float(input("Ingrese el monto de la factura " + str(ingreso_factura) + ": "))
    while(precio_factura <= 0):
        precio_factura = float(input("Reingrese el monto de la factura " + str(ingreso_factura) + ": "))
    dicc_facturas[ingreso_factura] = precio_factura

pagar = input("¿Quiere pagar alguna factura? (si/no): ")

if(pagar.capitalize() == "Si"):
    numero_factura = int(input("Ingrese el número de factura a pagar ahora: "))
    eliminar = [numero for numero in dicc_facturas if numero == numero_factura]
    for numero in eliminar:
        total_pagado += dicc_facturas[numero]
        del dicc_facturas[numero]


while(pagar.capitalize() != "No"):
    pagar = input("¿Quiere seguir pagando? (si/no): ")
    if (pagar.capitalize() == "No"):
        break
    numero_factura = int(input("Ingrese el número de factura a pagar ahora: "))
    eliminar = [numero for numero in dicc_facturas if numero == numero_factura]
    for numero in eliminar:
        total_pagado += dicc_facturas[numero]
        del dicc_facturas[numero]

for numero, precio in dicc_facturas.items():
    total_pendiente += precio

print("\n" + "Total pagado $" + str(total_pagado) + "\n")
print("Total pendiente $" + str(total_pendiente) + "\n")
print("Facturas pendientes:")
print(dicc_facturas)


# Solución de la guía:

"""
facturas = {}
cobrado = 0
pendiente = 0
more = ''
while more != 'T':
    if more == 'A':
        clave = input('Introduce el número de la factura: ')
        coste = float(input('Introduce el coste de la factura: '))
        facturas[clave] = coste
        pendiente += coste
    if more == 'P':
        clave = input('Introduce el número de la factura a pagar: ')
        coste = facturas.pop(clave, 0)
        cobrado += coste
        pendiente -= coste
    print('Recaudado:', cobrado)
    print('Pendiente de cobro: ', pendiente)
    more = input('¿Quieres añadir una nueva factura (A), pagarla (P) o terminar (T)? ')
"""


