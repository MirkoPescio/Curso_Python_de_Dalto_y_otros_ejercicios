"""
Ejercicio 2
Escribir un programa que pregunte el nombre completo del usuario en la consola
y después muestre por pantalla el nombre completo del usuario tres veces, 
una con todas las letras minúsculas, otra con todas las letras mayúsculas y 
otra solo con la primera letra del nombre y de los apellidos en mayúscula. 
El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
"""

# Mi solución:

input_nombre = input("Ingrese su nombre: ")
input_apellido = input("Ingrese su apellido: ")

while len(input_nombre) <= 2 | len(input_apellido) <= 2:
    input_nombre = input("Ingrese un nombre válido: ")
    input_apellido = input("Ingrese un apellido válido: ")


CONTADOR = 3

nombre_completo = input_nombre + " " + input_apellido

for i in range(1, CONTADOR + 1):
    print("Ejecución número: " + str(i))
    print("Nombre completo: " + nombre_completo.lower())

for f in range(1, CONTADOR + 1):
    print("Ejecución número: " + str(f))
    print("Nombre completo: " + nombre_completo.upper())

for u in range(1, CONTADOR + 1):
    print("Ejecución número: " + str(u))
    print("Nombre completo: " + input_nombre.capitalize() + " " + input_apellido.capitalize())




# Solución de la guía:

"""
name = input("¿Cómo te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())
"""
