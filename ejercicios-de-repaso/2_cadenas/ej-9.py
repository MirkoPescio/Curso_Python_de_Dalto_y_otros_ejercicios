"""
Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato 
dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa 
anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

# Mi solución:

"ITEM 1)"

fecha_de_nacimiento_1 = input("Ingrese su fecha de nacimiento con el formato (dd/mm/aaaa): ")
dia_1 = fecha_de_nacimiento_1[0:1+1]
mes_1 = fecha_de_nacimiento_1[3:4+1]
año_1 = fecha_de_nacimiento_1[6:9+1]
respuesta_1 = "Usted nació el día " + dia_1 + " del mes " + mes_1 + " en el año " + año_1
print(respuesta_1)

"ITEM 2)"

fecha_de_nacimiento_2 = input("Ingrese su fecha de nacimiento con el formato (día/mes/año): ")
array_fecha_nacimiento = fecha_de_nacimiento_2.split("/")
dia_2 = array_fecha_nacimiento[0]
mes_2 = array_fecha_nacimiento[1]
año_2 = array_fecha_nacimiento[2]
respuesta_2 = "Usted nació el día " + dia_2 + " del mes " + mes_2 + " en el año " + año_2
print(respuesta_2)


# Solución de la guía:

"ITEM 1)"

fecha = input("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])

"ITEM 2)"

fecha = input("Introduce la fecha de tu nacimiento en formato día/mes/año: ")
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', dia)
print('Mes', mes)
print('Año', año)

