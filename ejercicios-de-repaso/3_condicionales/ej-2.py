"""
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres
contraseña en una variable, pregunte al usuario por la contraseña
e imprima por pantalla si la contraseña introducida por el usuario
coincide con la guardada en la variable sin tener en cuenta
mayúsculas y minúsculas.
"""

# Mi solución:

CONTRASEÑA_ALMACENADA = "CalleFalsa123"

contraseña_usuario = input("Ingrese la contraseña: ")

comparacion_1 = CONTRASEÑA_ALMACENADA.lower()
comparacion_2 = contraseña_usuario.lower()

if (comparacion_1 == comparacion_2):
    print("Acceso concedido!!")
else:
    print("Acceso denegado")


# Solución de la guía:

key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

