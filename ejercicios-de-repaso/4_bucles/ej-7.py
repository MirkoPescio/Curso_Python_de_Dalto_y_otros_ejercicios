"""
Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

# Mi solución:

contador = 1

while contador <= 10:
    for i in range(1, 10+1):
        resultado_multiplicacion = contador * i
        tabla_multiplicacion = str(contador) + " * " + str(i) + " = " + str(resultado_multiplicacion)
        print(tabla_multiplicacion)
    print("\n")
    contador += 1


# Solución de la guía:

"""
for i in range(1, 11):
    for j in range(1, 11):
        print(i*j, end="\t")
    print("")
"""

