"""
Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

# Mi solución:

dict_datos_personales = {}
nombre = input("Ingrese su nombre: ")

edad = int(input("Ingrese su edad: "))

while(edad <= 0):
    edad = int(input("Reingrese su edad: "))
    
direccion = input("Ingrese su dirección: ")
telefono = input("Ingrese su número de teléfono: ")

dict_datos_personales["nombre"] = nombre
dict_datos_personales["edad"] = edad
dict_datos_personales["dirección"] = direccion
dict_datos_personales["teléfono"] = telefono

print(dict_datos_personales["nombre"] + " tiene " + str(dict_datos_personales["edad"]) + " años, vive en " + dict_datos_personales["dirección"] + " y su número de teléfono es: " + dict_datos_personales["teléfono"])


# Solución de la guía:

"""
nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')
persona = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}
print(persona['nombre'], 'tiene', persona['edad'], 'años, vive en', persona['direccion'], 'y su número de teléfono es', persona['telefono'])
"""

