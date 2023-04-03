"""
El Timing para ver los conseptos básicos en Python es de 2.5 horas como mínimo, 7
horas como máximo y 4 horas en promedio; Sin embargo, el curso de Dalto sólo tomó
1.5 horas para ver dichos conceptos.

A) Cuanta diferencia hay en pocentaje entre el curso actual y:
   * El más rapido de los cursos
   * El más lento de los cursos
   * El promedio de los cursos
   
Teniendo en cuenta que el tiempo del crudo de los videos de los demás cursos en
promedio es de 5 horas y con edición es de 4 horas, mientras que el del video de
Dalto es de 3.5 y 1.5 horas respectivamente

B) Calcule el porcentaje de material inservible se reduce en:
   * El promedio de los cursos
   * El curso actual (El de Soy Dalto)
   
C) Ver 10 horas de este curso ¿a cuantas de otros cursos equivale? ¿Y al revés?
"""

# Mi solución:
print("MI SOLUCION")

### Datos para ver conceptos básicos de Python (otros cursos y Dalto)

min_otros_cursos = 2.5
max_otros_cursos = 7
prom_otros_cursos = 4
tiempo_basico_Dalto = 1.5

### Item A)

porcentaje_subitem_1 = ((max_otros_cursos - tiempo_basico_Dalto) / tiempo_basico_Dalto) * 100
porcentaje_subitem_2 = ((min_otros_cursos - tiempo_basico_Dalto) / tiempo_basico_Dalto) * 100
porcentaje_subitem_3 = ((prom_otros_cursos - tiempo_basico_Dalto) / tiempo_basico_Dalto) * 100
print(str(porcentaje_subitem_1) + "%")
print(str(porcentaje_subitem_2) + "%")
print(str(porcentaje_subitem_3) + "%")

### Item B)

otros_sin_edicion = 5
otros_con_edicion = 4
dalto_sin_edicion = 3.5
dalto_con_edicion = 1.5

porcentaje_reduccion_material_otros = ((otros_sin_edicion - otros_con_edicion) / otros_sin_edicion) * 100
porcentaje_reduccion_material_dalto = ((dalto_sin_edicion - dalto_con_edicion) / dalto_sin_edicion) * 100

print("El porcentaje de reducción de material de otros cursos de Python es del " + str(porcentaje_reduccion_material_otros) + "%")
print("El porcentaje de reducción de material del curso de Python de Dalto es del " + str(porcentaje_reduccion_material_dalto) + "%")


### Item C)

tiempo_promedio_curso_de_Dalto = 1.5
tiempo_promedio_otros = 4
tiempo_curso_de_Dalto_a_invertir = float(input("Ingrese la cantidad de horas que invertirá viendo cursos de Dalto: "))

while(tiempo_curso_de_Dalto_a_invertir <= 0):
    tiempo_curso_de_Dalto_a_invertir = float(input("Reingrese un valor válido (tiempo en horas): "))

tiempo_curso_de_otros_a_invertir = float(input("Ingrese la cantidad de horas que invertirá viendo cursos de otros: "))

while(tiempo_curso_de_otros_a_invertir <= 0):
    tiempo_curso_de_otros_a_invertir = float(input("Reingrese un valor válido (tiempo en horas): "))

calculo_tiempo = (tiempo_curso_de_Dalto_a_invertir * tiempo_promedio_otros) / tiempo_promedio_curso_de_Dalto
calculo_tiempo_al_reves = (tiempo_curso_de_otros_a_invertir * tiempo_promedio_curso_de_Dalto) / tiempo_promedio_otros

print("Ver " + str(tiempo_curso_de_Dalto_a_invertir) + " horas en cursos de Dalto equivalen a ver " + str(round(calculo_tiempo, 2)) + " horas de otros cursos (Del mismo tema)")
print("Ver " + str(tiempo_curso_de_otros_a_invertir) + " horas en cursos de otros equivalen a ver " + str(round(calculo_tiempo_al_reves, 2)) + " horas en el curso de Dalto (Del mismo tema)")

print("\n")

# Solución de Dalto:

print("SOLUCION DE DALTO")

## Valores de duración de cursos:

otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

## Diferencias de duración:

diferencia_con_min = 100 - (dalto_curso / otros_cursos_min * 100)
diferencia_con_max = 100 - (dalto_curso / otros_cursos_max * 100)
diferencia_con_promedio = 100 - (dalto_curso / otros_cursos_promedio * 100)

print(f'El curso de Dalto dura un {diferencia_con_min}% menos que el más rápido de los otros cursos')
print(f'El curso de Dalto dura un {round(diferencia_con_max, 2)}% menos que el más lento de los otros cursos')
print(f'El curso de Dalto dura un {diferencia_con_promedio}% menos que el promedio de los otros cursos')

## Duración de crudos:

crudo_promedio = 5
crudo_dalto = 3.5

## Calculando el porcentaje de tiempo vacío removido:

tiempo_vacio_promedio = 100 - (otros_cursos_promedio / crudo_promedio * 100)
tiempo_vacio_Dalto = 100 - (dalto_curso / crudo_dalto * 100)

print(f'La diferencia de tiempo vacío removido de un curso promedio es del {tiempo_vacio_promedio}%')
print(f'La diferencia de tiempo vacío removido de un curso de Dalto es del {round(tiempo_vacio_Dalto, 2)}%')

## Mostrando diferencias si los cursos duraran 10 horas:

print(f'Ver 10 horas de un curso de Dalto equivalen a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otro curso equivalen a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de un curso de Dalto')

