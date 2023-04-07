"""
Hoy faltó el profesor de clases y los alumnos organizaron armar su propia clase.
Uno de ellos va a ser el profesor y el otro va a ser su asistente.

A) Pedir la edad de los compañeros que vinieron hoy a clase y ordenar los datos de
menor a mayor

B) El mayor es el profesor y el menor es el asistente. ¿Quién es quién?
"""

# Mi Solución:

def ingreso_edades(cantidad_alumnos):
    lista_edades = []
    ingreso = ""
    for i in range(1, cantidad_alumnos+1):
        ingreso = int(input(f"Ingrese la edad del alumno n° {i}: "))
        while(ingreso <= 6):
            ingreso = int(input(f"Reingrese la edad del alumno n° {i}: "))
        lista_edades.append(ingreso)
    lista_edades.sort()
    return lista_edades

def mayor_y_menor(lista_edades_ordenada):
    mayor = lista_edades_ordenada[-1]
    menor = lista_edades_ordenada[0]
    return (mayor, menor)

def main():
    cantidad_alumnos = int(input("Ingresar la cantidad de alumnos del curso (mínimo 5): "))
    while(cantidad_alumnos < 5):
        cantidad_alumnos = int(input("Reingresar la cantidad de alumnos del curso (MINIMO 5): "))
    lista_final = ingreso_edades(cantidad_alumnos)
    tupla_item_b = mayor_y_menor(lista_final)
    profesor_y_asistente = f'El profesor (alumno mayor) tiene {tupla_item_b[0]} años y el asistente (alumno menor) tiene {tupla_item_b[1]} años'
    print(lista_final)
    print(profesor_y_asistente)
main()


# Solución de Dalto:

def obtener_compañeros(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("Ingrese el nombre del alumno: ")
        edad = int(input("Ingrese la edad del alumno: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1]) # Ordena la lista según la edad
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asistente, profesor = obtener_compañeros(5)

print(f'El profesor es {profesor} y el asistente es {asistente}')

