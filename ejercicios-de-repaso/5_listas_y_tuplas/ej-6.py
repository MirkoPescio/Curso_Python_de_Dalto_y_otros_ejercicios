"""
Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista
las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las
asignaturas que el usuario tiene que repetir.
"""

# Mi solución:

lista_asignaturas = ["Matemáticas", "Física", "Química", "Algebra", "Programación 1"]
nota = ""

for i in range(len(lista_asignaturas)-1, -1, -1):
    nota = float(input("Ingrese la nota que sacó en " + lista_asignaturas[i] + ": "))
    while((nota < 0) or (nota > 10)):
         nota = float(input("Reingrese la nota que sacó en " + lista_asignaturas[i] + ": "))
    if (nota >= 7 and nota <= 10):
        lista_asignaturas.pop(i)

if (len(lista_asignaturas) == 0):
    print("\n" + "No tenés materias desaprobadas")
else:
    print("\n" + "Materias a repetir: " + "\n")
    for materia in lista_asignaturas:
        print(materia)
        

# Solución de la guía:

"""
### Solución 1:

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
passed = []
for subject in subjects:
    score = float(input("¿Qué nota has sacado en " + subject + "?"))
    if score >= 5:
        passed.append(subject)
for subject in passed:
    subjects.remove(subject)
print("Tienes que repetir " + str(subjects))

### Solución 2:

subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for i in range(len(subjects)-1, -1, -1):
    score = float(input("¿Qué nota has sacado en " + subjects[i] + "?"))
    if score >= 5:
        subjects.pop(i)
print("Tienes que repetir " + str(subjects))
"""

