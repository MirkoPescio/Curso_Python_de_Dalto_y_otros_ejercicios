"""
Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre
por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura>
es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario.
"""

# Mi solución:

lista_asignaturas = ["Matemáticas", "Física", "Química", "Algebra", "Programación 1"]
nota = ""

for materia in lista_asignaturas:
    nota = float(input("Ingrese la nota de la materia " + materia + ": "))
    while(nota < 0 or nota > 10):
        nota = float(input("Reingrese la nota de la materia " + materia + ": "))
    print("Nota obtenida en la materia " + materia + ": " + str(nota))


# Solución de la guía:

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])
