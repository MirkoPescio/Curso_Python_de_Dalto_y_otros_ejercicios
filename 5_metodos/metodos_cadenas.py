cadena_1 = "Hola Mundo!!"
cadena_2 = "Buenas Trevor, soy chavales!!"
cadena_3 = "1158069724"
cadena_4 = "Cadenadetextoynúmeros1231234"
cadena_5 = "SoloTexto"

# print(dir(cadena_1)) # Muestra diferentes métodos que se le pueden aplicar a éste tipo de dato
# print(dir(["lista", "de", "datos"])) # en el caso de la lista, me va a dar otros métodos
# Lo mismo para números enteros (int), flotantes (float), sets, diccionarios, entre otros

"""
Una aclaración antes de pasar con los métodos, dir no es un método, sino una fúnción de Python.
Los métodos se aplican seguido del dato, ¿cómo?, con la siguiente nomenclatura:
tipo_de_dato.metodo()  ó   variable.metodo()

Vamos a ver algunos para los Strings
"""

# upper: convierte todo el texto a mayúsculas

print(cadena_2.upper())

# lower: convierte todo el texto a minúsculas

print(cadena_2.lower())

# Capitalize: primero convierte todo el texto a minúsculas y después el primer caracter lo pasa a mayúsculas

print(cadena_1.capitalize())

# find: buscamos una cadena en otra cadena, si no hay coincidencias devuelve -1

print(cadena_2.find("Trev"))
print(cadena_2.find("d"))
print(cadena_2.find("a")) # en este caso "a" está 2 veces en la cadena, pero va a devolver sólo el 1er resultado que encuentre

# index: es igual a find, con la diferencia de que si no hay coincidencias lanza una excepción

print(cadena_1.index("M"))
print(cadena_1.index("Hola"))

# isNumeric: si es numérico, devuelve True, de lo contrario, devuelve False

print(cadena_1.isnumeric())
print(cadena_2.isnumeric())
print(cadena_3.isnumeric())
print(cadena_4.isnumeric())

# isAlpha: si es alfabético (sólo texto a-z), devuelve True, de lo contrario, devuelve False

print(cadena_1.isalpha())
print(cadena_2.isalpha())
print(cadena_3.isalpha())
print(cadena_4.isalpha())
print(cadena_5.isalpha())

# isalnum: si es alfanúmerico, devuelve True, de lo contrario, devuelve False

print(cadena_1.isalnum())
print(cadena_2.isalnum())
print(cadena_3.isalnum())
print(cadena_4.isalnum())
print(cadena_5.isalnum())

"Recordar que el espacio, " ", NO ES alfanúmerico"

# count: devuelve el número de ocurrencias de una subcadena en la cadena dada

print(cadena_1.count("o"))
print(cadena_2.count("o"))
print(cadena_3.count("o"))
print(cadena_4.count("o"))
print(cadena_5.count("o"))

# len: cuenta la cantidad de caractéres que tiene una cadena. No es un método sino una función

print(len(cadena_1))
print(len(cadena_2))
print(len(cadena_3))
print(len(cadena_4))
print(len(cadena_5))

# startswith: verificamos si una cadena empieza con una cadena dada. Si es así devuelve True, de lo contrario False

print(cadena_1.startswith("H")) #True
print(cadena_2.startswith("Trevor")) #False
print(cadena_3.startswith("115")) #True
print(cadena_4.startswith("cadena")) # False
print(cadena_5.startswith("solotexto")) # False


# endswith: verificamos si una cadena termina con una cadena dada. Si es así devuelve True, de lo contrario False

print(cadena_1.endswith("!!")) #True
print(cadena_2.endswith("!!")) #True
print(cadena_3.endswith("!!")) #False
print(cadena_4.endswith("!!")) #False
print(cadena_5.endswith("!!")) #False

# replace: si el valor 1, se encuentra en la cadena original, reemplaza el valor 1 de la misma, por el valor 2

cadena_por_comas = "buenos/as,días/tardes/noches,¿cómo,están?"
cadena_replace = cadena_por_comas.replace(",", " ")
cadena_replace_final = cadena_replace.capitalize()
print(cadena_replace_final)

# split: separa cadenas con la cadena que le pasemos
# Este método, a diferencia de los demás, es el único que al aplicarlo nos va a devolver una matriz (lista)

cadena_matriz = cadena_por_comas.split(",")
print(cadena_matriz)
print(type(cadena_matriz))


