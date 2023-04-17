"""
Ejercicio 7
Escribir una función que reciba un diccionario con las asignaturas y las notas de 
un alumno y devuelva otro diccionario con las asignaturas en mayúsculas y las 
calificaciones correspondientes a las notas.
"""

# Mi solución:

def funcion_ingreso_asignaturas():
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

def funcion_definir_calificaciones(diccionario_materias):
    diccionario_final = {}
    for materia, nota in diccionario_materias.items():
        if(nota < 7):
            diccionario_final[materia.upper()] = (nota, "Desaprobado")
        else:
            diccionario_final[materia.upper()] = (nota, "Aprobado")
    return diccionario_final

def main():
    diccionario_inicial = funcion_ingreso_asignaturas()
    diccionario_final = funcion_definir_calificaciones(diccionario_inicial)
    print("EL DICCIONARIO FINAL DE CALIFICACIONES ES:")
    print(diccionario_final)
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

def apply_grade(scores):
    '''
    Función que recibe un diccionario de asignaturas y notas y devuelve otro con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
    Parámetros:
        scores: Es un diccionario con pares asignatura:nota donde nota es un valor real entre 0 y 10.
    Devuelve
        Un diccionario con pares ASIGNATURA:calificación, donde calificación es la calificación correspondiente a la nota de la asignatura.
    '''
    subjects = map(str.upper, scores.keys())
    grades = map(grade, scores.values())
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
    return {subject.upper():grade(score) for subject, score in scores.items()}

print(apply_grade({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))
