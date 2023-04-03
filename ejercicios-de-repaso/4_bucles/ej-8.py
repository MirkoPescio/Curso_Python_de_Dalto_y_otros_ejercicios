"""
Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
"""

# Mi solución:

"""
num = int(input("Ingrese un número entero positivo: "))

while(num <= 0):
    num = int(input("TE DIJE POSITIVO: "))

string_triangulo_rectangulo = ""

for i in range(1, num+1, 2):
    string_triangulo_rectangulo += str(i) + " "
    print(string_triangulo_rectangulo[::-1])

"""

# Solución de la guía:


n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end=" ")
    print("")
    
