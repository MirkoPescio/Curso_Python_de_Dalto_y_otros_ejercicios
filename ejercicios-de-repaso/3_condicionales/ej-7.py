"""
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un
determinado país son los siguientes:

Renta                   Tipo impositivo
Menos de 10000€              5%
Entre 10000€ y 20000€        15%
Entre 20000€ y 35000€        20%
Entre 35000€ y 60000€        30%
Más de 60000€                45%

Escribir un programa que pregunte al usuario su renta anual
y muestre por pantalla el tipo impositivo que le corresponde.
"""

# Mi solución:

monto_de_renta = float(input("Ingrese el valor mensual de su renta: "))

while (monto_de_renta <= 0):
    print("Error! Monto inválido")
    monto_de_renta = float(input("Reingrese el valor mensual de su renta: "))

if (monto_de_renta < 10000):
    print("Su valor impositivo es del 5%")
elif ((monto_de_renta >= 10000) and (monto_de_renta < 20000)):
    print("Su valor impositivo es del 15%")
elif ((monto_de_renta >= 20000) and (monto_de_renta < 35000)):
    print("Su valor impositivo es del 20%")
elif ((monto_de_renta >= 35000) and (monto_de_renta < 60000)):
    print("Su valor impositivo es del 30%")
else:
    print("Su valor impositivo es del 45%")


# Solución de la guía:

"""
# Preguntar al usuario por la renta
renta = float(input("¿Cuál es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45
# Mostrar por pantalla el producto de la renta por el tipo impositivo
print("Tienes que pagar ", renta * tipo / 100, "€", sep='')
"""
