"""
Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión.
"""

# Mi solución

capital = float(input("Ingrese el capital a invertir: "))

while capital <= 0:
    capital = float(input("Reingrese un valor de capital válido: "))

interes_anual = float(input("Ingrese el porcentaje de interés anual: "))

while interes_anual < 0:
    interes_anual = float(input("Reingrese un porcentaje válido: "))

tiempo = int(input("Ingrese el tiempo a invertir (en años): "))

while tiempo <= 0:
    tiempo = int(input("Reingrese un tiempo válido: "))

capital_obtenido = capital * (interes_anual / 100 + 1) * tiempo

print("El cápital obtenido es de $" + str(capital_obtenido))


# Solución de la página web:

"""
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))
print("Capital final: " + str(round(cantidad * (interes / 100 + 1) ** años, 2)))
"""