"""
Ejercicio 3
Escribir un programa que pregunte el nombre del usuario en la consola y después de que
el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE>
es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.
"""

# Mi solución:

NOMBRE = input("Ingrese su nombre de usuario: ")

while len(NOMBRE) <= 3:
    print("Ingrese un nombre de usuario válido")
    print("MINIMO 3 CARACTERES")
    NOMBRE = input("Reingrese el nombre de usuario: ")

n = len(NOMBRE)

respuesta = "El nombre de usuario ingresado: " + NOMBRE.upper() + " tiene " + str(n) + " caracteres"
print(respuesta)

# Solución de la guía:

nombre = input("¿Cómo te llamas? ")
print(nombre.upper() + " tiene " + str(len(nombre)) + " letras")


