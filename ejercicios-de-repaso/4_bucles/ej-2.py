"""
Ejercicio 2
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos
los años que ha cumplido (desde 1 hasta su edad).
"""

# Mi solución:

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

print("Buenas " + nombre + "!! Va un conteo de tu edad:")

for i in range(edad + 1):
    print(i)


# Solución de la guía:

"""
age = int(input("¿Cuántos años tienes? "))
for i in range(age):
    print("Has cumplido " + str(i+1) + " años")
"""

