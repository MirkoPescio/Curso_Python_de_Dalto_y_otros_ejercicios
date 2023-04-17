"""
Ejercicio 10
Una inmobiliaria de una ciudad maneja una lista de inmuebles como la siguiente:

[{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
{'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
{'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
{'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
{'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra 
lista con los inmuebles cuyo precio sea menor o igual que el dado. 
Los inmuebles de la lista que se devuelva deben incorporar un nuevo par a cada diccionario 
con el precio del inmueble, donde el precio de un inmueble se calcula con las siguiente 
fórmula en función de la zona:

Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
"""

# Mi solución:

AÑO_ACTUAL = 2023

def agregar_precio(lista_total_inmuebles):
    precio = ""
    validez_garaje = 0
    antiguedad = ""
    for diccionario in lista_total_inmuebles:
        antiguedad = AÑO_ACTUAL - diccionario["año"]
        if(diccionario["garaje"] == True):
            validez_garaje = 1
        if(diccionario["zona"] == "A"):
            precio = (diccionario["metros"] * 1000 + diccionario["habitaciones"] * 5000 + validez_garaje * 15000) * (1-antiguedad/100)
        elif(diccionario["zona"] == "B"):
            precio = (diccionario["metros"] * 1000 + diccionario["habitaciones"] * 5000 + validez_garaje * 15000) * (1-antiguedad/100) * 1.5
        diccionario["precio"] = precio
    return lista_total_inmuebles

def filtrar_lista_inmuebles(lista_total_inmuebles):
    presupuesto = float(input("Ingrese su presupuesto a invertir en un inmueble ($): "))
    while(presupuesto <= 0):
        presupuesto = float(input("Reingrese el presupuesto a invertir en un inmueble: "))
    lista_filtrada = []
    for diccionario in lista_total_inmuebles:
        if (diccionario["precio"] <= presupuesto):
            lista_filtrada.append(diccionario)
    return lista_filtrada

def main():
    lista_total_de_inmuebles = [
        {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
        {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
        {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
        {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
        {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
    ]
    lista_con_precio_de_inmuebles = agregar_precio(lista_total_de_inmuebles)
    print("LA LISTA DE LOS INMUEBLES QUE PUEDE ELEGIR ES LA SIGUIENTE:")
    print(lista_con_precio_de_inmuebles)
    presupuesto_a_invertir = filtrar_lista_inmuebles(lista_con_precio_de_inmuebles)
    print("SEGUN SU PRESUPUESTO, LOS INMUEBLES A LOS QUE PUEDE ACCEDER SON:")
    print(presupuesto_a_invertir)
main()

print("\n")

# Solución de la guía:

pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtro,map(añadir_precio, pisos)))

print(busca_piso(pisos, 100000))

