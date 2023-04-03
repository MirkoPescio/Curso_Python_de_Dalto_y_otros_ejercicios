"""
Escribir un programa que lea un entero positivo,
n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta
n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: [n(n+1)/2]
"""

# Mi solución

num = int(input("Ingrese un número entero positivo: "))

while num <= 0:
    num = int(input("Reingrese el número: "))

for i in range (1, num + 1):
    print(i)

calculo = int(num*(num+1)/2)

for u in range(1, calculo + 1):
    print(u)


# Solución de la página web:

"""
n = int(input("Introduce un número entero: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números enteros desde 1 hasta " + str(n) + " es " + str(suma))
"""