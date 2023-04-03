"""
Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre
por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
"""

# Mi solución:

num1 = float(input("Ingrese un número: "))
num2 = float(input("Ingrese otro número: "))

if (num2 == 0):
    print("Error algorítmico"+ "\n" + "En la división el divisor NUNCA puede ser 0 (cero)")

calculo_resto_division = num1 / num2

print("Resultado de la división: " + str(calculo_resto_division))


# Solución de la guía:

"""
n = float(input("Introduce el dividendo: "))
m = float(input("Introduce el divisior: "))
if m == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(n/m)
"""

