"""
Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono,
correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un
nuevo dato debe imprimirse el contenido del diccionario.
"""

# Mi solución:

print("Ingreso de datos de personas")

dicc_datos_personas = {}

nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
while(edad <= 0 or edad > 120):
    edad = int(input("Reingrese la edad: "))
sexo = input("Ingrese el sexo: ")
telefono = input("Ingrese el número de teléfono: ")
correo_electronico = input("Ingrese el correo electrónico: ")
ingreso = ""

dicc_datos_personas["persona 1"] = nombre, edad, sexo, telefono, correo_electronico
contador = 1

while(ingreso.lower() != "no"):
    ingreso = input("¿Quiere seguir ingresando datos? (si/no): ")
    if (ingreso.lower() == "no"):
        break
    print("Nuevo registro de datos")
    contador += 1
    nombre = input("Ingrese el nombre: ")
    edad = int(input("Ingrese la edad: "))
    while(edad <= 0 or edad > 120):
        edad = int(input("Reingrese la edad: "))
    sexo = input("Ingrese el sexo: ")
    telefono = input("Ingrese el número de teléfono: ")
    correo_electronico = input("Ingrese el correo electrónico: ")
    dicc_datos_personas[str("persona " + str(contador))] = nombre, edad, sexo, telefono, correo_electronico

print(dicc_datos_personas)
    

# Solución de la guía:

persona = {}
continuar = True
while continuar:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    persona[clave] = valor
    print(persona)
    continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

