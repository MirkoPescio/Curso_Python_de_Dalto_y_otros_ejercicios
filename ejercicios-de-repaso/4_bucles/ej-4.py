"""
Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""

# Mi solución:

num = int(input("Ingrese un número entero positivo: "))

while (num <= 0):
    num = int(input("TE DIJE POSITIVO: "))
    
print("Te mostramos por consola los números desde el " + str(num) + " hasta el 0")

cuenta_regresiva = ""

for i in range(0, num+1):
    cuenta_regresiva += str(num-i) + ", "
    
print(cuenta_regresiva)


# Solución de la guía:

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")
    


