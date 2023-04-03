"""
Ejercicio 1
Escribir un programa que pregunte el nombre del usuario en la consola y un 
número entero e imprima por pantalla en líneas distintas el nombre del usuario 
tantas veces como el número introducido.
"""

# Mi solución:

nombre_de_usuario = input("Ingrese su nombre de usuario: ")
contador_de_ejecucion = int(input("Ingrese la cantidad de ejecuciones del programa: "))

while contador_de_ejecucion <= 0:
    print("NUMEROS ENTEROS Y POSITIVOS")
    contador_de_ejecucion = int(input("Ingrese un valor válido para el contador de ejecución: "))

for i in range(1, contador_de_ejecucion + 1):
    print("ejecución número: " + str(i))
    print(nombre_de_usuario)


# Solución de la guía:

"""
nombre = input("¿Cómo te llamas? ")
n = input("Introduce un número entero: ")
print((nombre + "\n") * int(n))
"""
