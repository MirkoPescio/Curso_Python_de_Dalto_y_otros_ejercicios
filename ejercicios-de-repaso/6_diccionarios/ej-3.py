"""
Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas
de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre
por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en
el diccionario debe mostrar un mensaje informando de ello.

Fruta     Precio
Plátano    1.35
Manzana    0.80
Pera       0.85
Naranja    0.70
"""

# Mi solución:

dict_frutas = {}
eleccion_fruta = input("Ingrese una fruta a comprar: ")
numero_kilos = float(input("Ingrese el número de kilos a llevar: "))

while(numero_kilos <= 0):
    numero_kilos = float(input("Reingrese el número de kilos a llevar: "))

dict_frutas["Banana"] = 1.35
dict_frutas["Manzana"] = 0.80
dict_frutas["Pera"] = 0.85
dict_frutas["Naranja"] = 0.70

coincidencia = ""
contador = 0

for clave, valor in dict_frutas.items():
    if(eleccion_fruta.capitalize() == clave):
        coincidencia = (clave, valor)
        calculo_precio = numero_kilos * coincidencia[1]
        contador += 1
        print("El total a pagar por " + eleccion_fruta + " es de $" + str(round(calculo_precio, 2)))

if(contador == 0):
    print("La fruta ingresada no se encuentra en el diccionario registrado")


# Solución de la guía:

"""
frutas = {'Plátano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '€')
else: 
    print("Lo siento, la fruta", fruta, "no está disponible.")
"""

