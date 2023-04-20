"""
Ejercicio 3
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con 
la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero.
Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

# Mi solución:

def funcion_ingresar_numero_tabla():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    while((numero < 1) or (numero > 10)):
        numero = int(input("Reingrese un numero ENTRE 1 Y 10: "))
    return numero

def funcion_ingresar_numero_de_linea():
    numero_linea = int(input("Ingrese el número de línea entre 1 y 10: "))
    while((numero_linea < 1) or (numero_linea > 10)):
        numero_linea = int(input("Reingrese el número de línea ENTRE 1 Y 10: "))
    return numero_linea

def leer_fichero_de_tabla_de_multiplicar(n, m):
    nombre_fichero = f'./ejercicios-de-repaso/9_ficheros/tabla-{n}.txt'
    try:
        archivo = open(nombre_fichero, "r")
    except FileNotFoundError:
        print(f'No existe el fichero con la tabla del {n}')
    else:
        lineas = archivo.readlines()
        linea_elegida = lineas[m]
        archivo.close()
        return linea_elegida
    
def main():
    numero_de_tabla = funcion_ingresar_numero_tabla()
    numero_de_linea = funcion_ingresar_numero_de_linea()
    fichero = leer_fichero_de_tabla_de_multiplicar(numero_de_tabla, numero_de_linea)
    print(fichero)
main()

# Solución de la guía:


