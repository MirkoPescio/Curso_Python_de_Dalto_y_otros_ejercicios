"""
Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
el nombre del mes.
"""

# Mi solución:

input_fecha = input("Ingrese la fecha en el formato (dd/mm/aaaa): ")
array_fecha = input_fecha.split("/")

dicc_fecha = {}

dicc_fecha["día"] = array_fecha[0]
dicc_fecha["mes"] = array_fecha[1]
dicc_fecha["año"] = array_fecha[2]

print("La fecha ingresada es: día-" + dicc_fecha["día"] + " mes-" + dicc_fecha["mes"] + " año-" + dicc_fecha["año"])


# Solución de la guía:

meses = {
    1:'enero',
    2:'febrero',
    3:'marzo',
    4:'abril',
    5:'mayo',
    6:'junio',
    7:'julio',
    8:'agosto',
    9:'septiembre',
    10:'octubre',
    11:'noviembre',
    12:'diciembre'
}

fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
fecha = fecha.split('/')
print(fecha[0], 'de', meses[int(fecha[1])], 'de', fecha[2])
