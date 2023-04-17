"""
Ejercicio 6
Escribir una función reciba una lista de notas y devuelva la lista de calificaciones
correspondientes a esas notas.
"""

# Mi solución:

def definir_calificaciones(nota):
    calificacion = ""
    if(nota < 7):
        calificacion = (nota, "Desaprobado")
    else:
        calificacion = (nota, "Aprobado")
    return calificacion

def cantidad_notas():
    cantidad_de_notas = int(input("Ingrese la cantidad de notas a registrar en el sistema: "))
    while(cantidad_de_notas <= 2):
        cantidad_de_notas = int(input("Reingrese la cantidad de notas a registrar en el sistema: "))
    return cantidad_de_notas

def lista_notas(cantidad_de_notas):
    lista_de_notas = []
    for i in range(1, cantidad_de_notas+1):
        nota = float(input(f"Ingrese la nota n°{i}: "))
        while((nota < 0) or (nota > 10)):
            nota = float(input(f"Reingrese la nota n°{i}: "))
        lista_de_notas.append(nota)
    return lista_de_notas

def main():
    cantidad_de_notas = cantidad_notas()
    lista_de_notas = lista_notas(cantidad_de_notas)
    lista_resultados_finales = []
    calificacion = ""
    for nota in lista_de_notas:
        calificacion = definir_calificaciones(nota)
        lista_resultados_finales.append(calificacion)
    print(lista_resultados_finales)
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
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return list(map(grade, scores))

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))
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
    Función que devuelve la calificación correspondiente a las notas de una lista dada.
    Parámetros:
        scores: Es una lista de valores reales entre 0 y 10.
    Devuelve
        La lista de calificaciones correspondiente a las notas de scores.
    '''
    return [grade(x) for x in scores]

print(apply_grade([6.5, 5, 3.4, 8.2, 2.1, 9.7, 10]))
