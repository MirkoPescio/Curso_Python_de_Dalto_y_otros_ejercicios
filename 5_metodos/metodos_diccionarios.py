diccionario_1 = {
    "nombre": "Mirko",
    "apellido": "Pescio",
    "capital": 125000
}

diccionario_2 = {
    "heroes": ["Spiderman", "Batman", "Ironman"],
    "antiheroes": ["Deadpool", "Nathan Drake", "Joel Miller"],
    "villanos": ["Thanos", "Venom", "Freezer", "Cell"]
}

diccionario_3 = {
    "juego": "Dead Space 2",
    "requisitos": {
        "ram": "2 GB",
        "almacenamiento": "9 GB",
        "targeta gráfica": "512 MB VRAM",
        "sistema": "Windows 7 o superior"
    },
    "categoria": "suspenso/terror"
}

# keys: Me devuelve una lista con los nombres de cada clave del diccionario (también sirve para iterar)

claves_1 = diccionario_1.keys()
claves_2 = diccionario_2.keys()
print(claves_1)
print(claves_2)

# get: le pasamos el nombre de una clave y nos devuelve su respectivo valor. Si no encuentra ninguna clave con el nombre dado, nos devuelve None

valor_1_obtenido = diccionario_1.get("nombre")
valor_2_obtenido = diccionario_1.get("capital")
valor_3_obtenido = diccionario_2.get("antiheroes")
print(valor_1_obtenido)
print(valor_2_obtenido)
print(valor_3_obtenido)
print(diccionario_2.get("civiles"))

# clear: vacía el diccionario

print(diccionario_3)
print(diccionario_3.clear())

# pop: elimina un elemento del diccionario

print(diccionario_1.pop("apellido"))
print(diccionario_2.pop("antiheroes"))
print(diccionario_1)
print(diccionario_2)

# items: nos devuelve un elemento dict_items, es decir, un diccionario iterable

diccionario_1_iterable = diccionario_1.items()
diccionario_2_iterable = diccionario_2.items()
print(diccionario_1_iterable)
print(diccionario_2_iterable)



