"""
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años
y tener unos ingresos iguales o superiores a 1000 € mensuales.
Escribir un programa que pregunte al usuario su edad y sus ingresos
mensuales y muestre por pantalla si el usuario tiene que tributar
o no.
"""

# Mi solución:

MONTO_TRIBUTARIO_OBLIGATORIO = 1000

edad_usuario = int(input("Ingrese su edad: "))

while (edad_usuario <= 0):
    print("Error")
    edad_usuario = int(input("Reingrese su edad: "))

ingresos_mensuales = float(input("Ingrese el monto de sus ingresos mensuales: "))

while (ingresos_mensuales < 0):
    print("Error")
    ingresos_mensuales = float(input("Reingrese el monto de sus ingresos mensuales: "))

if (edad_usuario < 16):
    print("No estás en edad de tributar")
else:
    if (ingresos_mensuales >= MONTO_TRIBUTARIO_OBLIGATORIO):
        print("Usted tiene que tributar")
    else:
        print("No está obligado a tributar")


# Solución de la guía:

"""
age = int(input("¿Cuál es tu edad? "))
income = float(input("¿Cuales son tus ingresos mensuales?"))
if age > 16 and income >= 1000:
    print("Tienes que cotizar")
else:
    print("No tienes que cotizar")
"""

