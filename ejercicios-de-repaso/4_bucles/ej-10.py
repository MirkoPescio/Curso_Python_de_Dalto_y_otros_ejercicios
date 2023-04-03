"""
Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no.
"""

# Mi solución:

num = int(input("Ingrese un número entero positivo: "))

while(num <= 0):
    num = int(input("TE DIJE POSITIVO: "))
    
contador_divisores = 0

for i in range(1, num+1):
    if(num % i == 0):
        contador_divisores += 1
        
if(contador_divisores == 2):
    print(str(num) + " es número primo")
else:
    print(str(num) + " no es número primo")


# Solución de la guía:

"""
n = int(input("Introduce un número entero positivo mayor que 2: "))
i = 2
while n % i != 0:
    i += 1
if i == n:
    print(str(n) + " es primo")
else:
    print(str(n) + " no es primo")
"""

