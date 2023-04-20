"""
Ejercicio 2
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt 
con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre 
por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
"""

# Mi solución:

def funcion_ingreso_numero_de_tabla():
    numero_tabla = int(input("Ingrese un número entre 1 y 10: "))
    while((numero_tabla < 1) or (numero_tabla > 10)):
        numero_tabla = int(input("Reingrese un número ENTRE 1 Y 10: "))
    return numero_tabla

def leer_fichero_de_tabla_de_multiplicar(n):
    nombre_fichero = f'./ejercicios-de-repaso/9_ficheros/tabla-{n}.txt'
    try:
        archivo = open(nombre_fichero, "r")
    except FileNotFoundError:
        print(f'No existe el fichero con la tabla del {n}')
    else:
        print(archivo.read())
        archivo.close()

def main():
    ingreso_numero_de_tabla = funcion_ingreso_numero_de_tabla()
    leer_fichero_de_tabla_de_multiplicar(ingreso_numero_de_tabla)
main()

# Solución de la guía:

## Solución 1:

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    f = open(nombre_fichero, 'r')
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
else:
    print(f.read())
    f.close()

## Solución 2:

n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
try: 
    with open(nombre_fichero, 'r') as f:
        print(f.read())
except FileNotFoundError:
    print('No existe el fichero con la tabla del', n)
