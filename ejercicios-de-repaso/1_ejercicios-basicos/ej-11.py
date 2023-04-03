"""
Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año.
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu
cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad
de ahorros tras el primer, segundo y tercer año. Redondear cada cantidad a dos decimales.
"""

# Mi solución:

dinero_depositado = float(input("Ingrese una cantidad de dinero a depositar: "))

while dinero_depositado <= 0:
    dinero_depositado = float(input("Reingrese un valor válido:"))

interes_anual = float(input("Ingrese el porcentaje de la tasa de interés (sólo números positivos): "))

while interes_anual <= 0:
    interes_anual = float(input("Reingrese un valor válido de interés anual (%)(sólo números POSITIVOS): "))

tasa_de_interes = interes_anual / 100 + 1

ahorro_primer_year = dinero_depositado * tasa_de_interes * 1
ahorro_segundo_year = dinero_depositado * tasa_de_interes * 2
ahorro_tercer_year = dinero_depositado * tasa_de_interes * 3

print("El dinero total obtenido tras 1 año de inversión es de $" + str(round(ahorro_primer_year, 2)))
print("El dinero total obtenido tras 2 años de inversión es de $" + str(round(ahorro_segundo_year, 2)))
print("El dinero total obtenido tras 3 años de inversión es de $" + str(round(ahorro_tercer_year, 2)))

# Error en el razonamiento

# Solución de la página web:

inversion = float(input("Introduce la inversión inicial: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))
