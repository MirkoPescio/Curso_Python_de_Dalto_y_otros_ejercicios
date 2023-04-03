"""
Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase:
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado redondeado con dos decimales.
"""

# Fórmula para el cálculo de índice de masa corporal:
# IMC = Peso / (Altura)**2

# Mi solución:

peso = float(input("Ingrese su peso (en KG): "))
altura = float(input("Ingrese su altura (en m): "))
IMC = peso / (altura)**2

print("Su índice de masa corporal es de: " + str(round(IMC, 2)))

# Solución de la página web:

"""
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))
"""
