"""
Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y
los muestre por pantalla en orden inverso separados por comas.
"""

# Mi solución:

### Solución en lista:

lista = []

for i in range(1, 10+1):
    lista.append(i)

lista.sort(reverse=True)
print(lista)

### Solución en String:

lista = []
string = ""

for i in range(1, 10+1):
    lista.append(i)

lista.sort(reverse=True)

for num in lista:
    string += str(num) + ", "

print(string)


# Solución de la guía:

### Solución 1:

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, 11):
    print(numbers[-i], end=", ")
"""

### Solución 2:

"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
for number in numbers:
    print(number, end=", ")
"""

