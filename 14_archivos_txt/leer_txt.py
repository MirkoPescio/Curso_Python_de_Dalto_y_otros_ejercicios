# Leer y escribir archivos TXT

archivo_sin_leer = open("./texto_de_Mirko.txt", encoding="UTF-8")

## Leer archivo completo:
# archivo = archivo_sin_leer.read()
# print(archivo)

"""
encoding="UTF-8" es una propiedad para mostrar caracteres que no se
encuentren en inglés
"""

# Leer línea por línea:
# lineas = archivo_sin_leer.readlines()

# Leer una sóla línea:
# linea = archivo_sin_leer.readline()
# print(linea)

"Con readline() también puedo leer por cantidad de caracteres"

# leer_10_caracteres = archivo_sin_leer.readline(10)
# leer_25_caracteres = archivo_sin_leer.readline(25)
leer_40_caracteres = archivo_sin_leer.readline(40)
print(leer_40_caracteres)

# Cuando terminamos de leer el archivo, tenemos que cerrarlo:
archivo_sin_leer.close()

# y si queremos volver a leer el archivo, tenemos que volver a abrirlo con open()

