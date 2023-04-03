"""
Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
anual y el número de años, y muestre por pantalla el capital obtenido en la
inversión cada año que dura la inversión.
"""

# Mi solución:

monto_a_invertir = float(input("Ingrese su monto a invertir: "))

while(monto_a_invertir <= 0):
    monto_a_invertir = float(input("Reingrese el monto a invertir: "))
    
interes_anual = float(input("Ingrese el porcentaje de interés anual: "))

while(interes_anual <= 0):
    interes_anual = float(input("Reingrese el porcentaje de interés anual: "))
    
años_de_inversión = int(input("Ingrese la cantidad de años de inversión: "))

while(años_de_inversión <= 0):
    años_de_inversión = int(input("Reingrese la cantidad de años de inversión: "))

for i in range(1, años_de_inversión+1):
    calculo_interes = (monto_a_invertir * interes_anual * i) / 100
    capital_obtenido = "El capital obtenido en el año " + str(i) + " es de $" + str(monto_a_invertir + calculo_interes)
    print(capital_obtenido)


# Solución de la guía:

amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años?"))
for i in range(years):
    amount *= 1 + interest / 100 
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))
