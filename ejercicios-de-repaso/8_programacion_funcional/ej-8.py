"""
Ejercicio 8
Escribir una función reciba un diccionario con las asignaturas y las notas de 
un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las 
calificaciones correspondientes a las notas aprobadas.
"""

# Mi solución:

def funcion_cargar_notas():
    diccionario = {}
    asignatura = ""
    nota = ""
    ingreso = ""
    while(ingreso.capitalize() != "No"):
        asignatura = input("Ingrese una asignatura/materia: ")
        nota = float(input(f"Ingrese la nota obtenida en la materia {asignatura}: "))
        while((nota < 0) or (nota > 10)):
            nota = float(input(f"Reingrese la nota obtenida en la materia {asignatura}: "))
        diccionario[asignatura] = nota
        ingreso = input("¿Quiere seguir ingresando materias/asignaturas? (Si/No): ")
    return diccionario

def funcion_filtrar_asignaturas(diccionario_notas):
    diccionario_notas_aprobadas = {}
    for materia, nota in diccionario_notas.items():
        if(nota >= 7):
            diccionario_notas_aprobadas[materia.upper()] = nota
    return diccionario_notas_aprobadas

def main():
    diccionario_inicial = funcion_cargar_notas()
    diccionario_asignaturas_aprobadas = funcion_filtrar_asignaturas(diccionario_inicial)
    nombre_alumno = input("Ingrese el nombre del/de la alumno/a: ")
    apellido_alumno = input("Ingrese el apellido del/de la alumno/a: ")
    print(f"LAS MATERIAS APROBADAS POR EL/LA ALUMNO/A {nombre_alumno} {apellido_alumno} SON:")
    print(diccionario_asignaturas_aprobadas)
main()

print("\n")

# Solución de la guía:

## Solución 1:

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def passed_subject(subject):
    '''
    Función que recibe una tupla con una asignatura y su nota y devuelve True si la asignatura está aprobada o False si está suspensa.abs
    Parámetros:
        subject: Es una tupla (asignatura, nota) donde nota es un valor real entre 0 y 10.
    Devuelve: True si la nota es mayor o igual que 5 y False si no.abs
    '''
    return (subject[1] >= 5)


def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    passed = dict(filter(passed_subject, scores.items()))
    subjects = map(str.upper, passed.keys())
    grades = map(grade, passed.values())
    return dict(zip(subjects, grades))

print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))
print("\n")

## Solución 2:

def grade(score):
    '''
    Función que devuelve la calificación correspondiente a una nota.
    Parámetros:
        score: Es un valor real entre 0 y 10.
    Devuelve:
        La calificación correspondiente a la nota score.
    '''
    if score < 5:
        return 'SS'
    elif score < 7:
        return 'AP'
    elif score < 9:
        return 'NT'
    elif score < 10:
        return 'SB'
    else:
        return 'MH'

def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    return {subject.upper():grade(score) for subject, score in scores.items() if score >= 5}

print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))
print("\n")
