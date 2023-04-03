"""
Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará.
"""

# Mi solución:

string = ""
consulta = ""
ingreso = input("Empiece a ingresar un texto: ")
string += ingreso

while(consulta.lower() != "salir"):
    consulta = input("¿Quiere seguir ingresando texto? (si/salir): ")
    if (consulta.lower() == "salir"):
        break
    ingreso = input("Continúe ingresando texto: ")
    string += "\n" + ingreso

print(string)


# Solución de la guía:

"""
while True:
    frase = input("Introduce algo: ")
    if frase == "salir":
        break
    print(frase)
"""

