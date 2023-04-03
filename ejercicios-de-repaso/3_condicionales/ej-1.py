"""
Ejercicio 1
Escribir un programa que pregunte al usuario su edad y muestre
por pantalla si es mayor de edad o no.
"""

# Mi solución:

edad_usuario = int(input("Ingrese su edad: "))

while (edad_usuario <= 0) or (edad_usuario >= 150):
    edad_usuario = int(input("Ingrese un número válido para la edad: "))

if (edad_usuario < 18):
    print("Sos menor de edad")
else:
    print("Sos mayor de edad")


# Solución de la guía:

age = int(input("¿Cuál es tu edad? "))
if age < 18: 
    print ("Eres menor de edad.")
else:
    print("Eres mayor de edad.")
    
