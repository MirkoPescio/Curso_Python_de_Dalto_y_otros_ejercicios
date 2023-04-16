"""
with open("./texto_de_Mirko.txt", "r"):
    print("Hola")
"""  

# De otra forma sería:

with open("./texto_de_Mirko.txt", encoding="UTF-8") as archivo:
    # Leemos el archivo:
    contenido = archivo.read()
    # Mostramos el contenido
    print(contenido)    

# No es necesario cerrar el archivo con with open



