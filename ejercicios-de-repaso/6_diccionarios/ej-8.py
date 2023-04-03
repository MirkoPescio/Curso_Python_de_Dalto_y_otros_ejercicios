import re
"""
Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés.
El usuario introducirá las palabras en español e inglés separadas por dos puntos,
y cada par <palabra>:<traducción> separados por comas.
El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla
palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

# Mi solución:

'''
dicc_traduccion = {
    "hola": "hello",
    "yo": "i",
    "código": "code",
    "usuario": "user",
    "contraseña": "password",
    "edad": "age",
    "años": "years",
    "año": "year",
    "ciudad": "city"
}
'''

dicc_traduccion = {}
palabra_español = input("Ingrese una palabra en español: ")
palabra_ingles = input("Ingrese su traducción en inglés: ")
dicc_traduccion[palabra_español] = palabra_ingles
ingreso = ""

while(ingreso.capitalize() != "No"):
    ingreso = input("¿Quiere seguir ingresando traducciones? (si/no): ")
    if(ingreso.capitalize() == "No"):
        break
    print("Ingreso de una nueva traducción:")
    palabra_español = input("Ingrese una palabra en español: ")
    palabra_ingles = input("Ingrese su traducción en inglés: ")
    dicc_traduccion[palabra_español] = palabra_ingles

frase = input("Ingrese una frase (en español para traducir a inglés): ")

for esp, eng in dicc_traduccion.items():
    frase = re.sub(esp, eng, frase)
        
print(dicc_traduccion)
print(frase)


# Solución de la guía:

"""
diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')
"""

