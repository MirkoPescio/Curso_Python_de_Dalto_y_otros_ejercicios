"""
Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
"""

# Mi solución:

CONTRASEÑA_DEL_PROGRAMA = "CRONOS"
ingreso = input("Ingrese la contraseña: ")
contador_errores = 0


while(ingreso.upper() != CONTRASEÑA_DEL_PROGRAMA):
    print("ERROR. Contraseña incorrecta")
    contador_errores += 1
    ingreso = input("Reingrese la contraseña: ")
    if (contador_errores == 2):
        print("INTRUSO DETECTADO")
        break

if(ingreso.upper() == CONTRASEÑA_DEL_PROGRAMA):
    print("Bienvenido/a!!")


# Solución de la guía:

"""
key = "contraseña"
password = ""
while password != key:
    password = input("Introduce la contraseña: ")
print("Contraseña correcta")
"""

