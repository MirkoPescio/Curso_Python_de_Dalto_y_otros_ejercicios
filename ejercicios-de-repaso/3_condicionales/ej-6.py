"""
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B
de acuerdo al sexo y el nombre. El grupo A esta formado por
las mujeres con un nombre anterior a la M y los hombres con un
nombre posterior a la N y el grupo B por el resto.
Escribir un programa que pregunte al usuario su nombre y sexo,
y muestre por pantalla el grupo que le corresponde.
"""

# Mi solución:

nombre_alumno = input("Ingrese su nombre: ")
genero = input("Ingrese su género (F/M): ")

letras_1 = "ABCDEFGHIJKL"
letras_2 = "ÑOPQRSTUVWXYZ"

if (genero.upper() == "F") and (letras_1.find(nombre_alumno[0]) != -1):
    print("Estás en el grupo A")
elif (genero.upper() == "M") and (letras_2.find(nombre_alumno[0]) != -1):
    print("Estás en el grupo A")
else:
    print("Estás en el grupo B")


# Solución de la guía:

"""
name = input("¿Cómo te llamas? ")
gender = input("¿Cuál es tu sexo (M o H)? ")
if gender == "M":
    if name.lower() < "m":
        group = "A"
    else:
        group = "B"
else:
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)
"""

