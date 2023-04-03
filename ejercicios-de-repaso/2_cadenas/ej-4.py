"""
Ejercicio 4
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
donde el prefijo es el código del país +34, y la extensión tiene dos dígitos 
(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono 
con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""

# Mi solución:

prefijo = int(input("Ingrese el prefijo de su número de teléfono: "))

while len(str(prefijo)) != 2:
    print("El prefijo de los teléfonos es de 2 caractéres")
    prefijo = int(input("Reingrese el prefijo: "))

numero = int(input("Ingrese su número de teléfono: "))

while len(str(numero)) != 10:
    print("La cantidad de caracteres de los números de teléfono es de 10")
    numero = int(input("Reingrese su número de teléfono: "))

extension = input("Ingrese la extensión de su número de teléfono (si no tiene ingrese 00): ")

while len(extension) != 2:
    print("La extensión de los números de teléfono no supera los 2 caracteres")
    extension = int(input("Reingrese la extensión del número de teléfono: "))

respuesta = "Su número de teléfono es: " + str(numero)
telefono_completo = "+" + str(prefijo) + "-" + str(numero) + "-" + str(extension)
print(respuesta)
print(telefono_completo)


# Solución de la guía:

tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])

