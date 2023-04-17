"""
Ejercicio 2
Escribir una función que simule una calculadora científica que permita calcular el 
seno, coseno, tangente, exponencial y logaritmo neperiano. La función preguntará al 
usuario el valor y la función a aplicar, y mostrará por pantalla una tabla con los 
enteros de 1 al valor introducido y el resultado de aplicar la función a esos enteros.
"""

import math

# Mi Solución:

def seno_coseno_y_tangente(num):
    seno = math.sin(num)
    coseno = math.cos(num)
    tangente = math.tan(num)
    return (seno, coseno, tangente)

def exponencial(num):
    exponente = int(input("FUNCION EXPONENCIAL. Ingrese un exponente: "))
    return (exponente, num ** exponente)

def logaritmo_neperiano(num):
    return math.log(num)

def main():
    num = float(input("Ingrese un número positivo: "))
    while(num <= 0):
        num = float(input("Reingrese un número POSITIVO: "))
    funcion = input("Ingrese la función a ejecutar (sin, cos, tan, exp, log): ")
    if(funcion.lower() == "sin"):
        seno = seno_coseno_y_tangente(num)[0]
        rta_1_a = f'El seno del número {num} es: {seno}'
        print(rta_1_a)
    elif(funcion.lower() == "cos"):
        coseno = seno_coseno_y_tangente(num)[1]
        rta_1_b = f'El coseno del número {num} es: {coseno}'
        print(rta_1_b)
    elif(funcion.lower() == "tan"):
        tangente = seno_coseno_y_tangente(num)[2]
        rta_1_c = f'La tangente del número {num} es: {tangente}'
        print(rta_1_c)
    elif(funcion.lower() == "exp"):
        exponente, exponencial_num = exponencial(num)
        rta_2 = f'{num} elevado al/a la {exponente} da como resultado: {exponencial_num}'
        print(rta_2)
    elif(funcion.lower() == "log"):
        logaritmo_base_e = logaritmo_neperiano(num)
        rta_3 = f'El logaritmo natural de {num} da como resultado: {logaritmo_base_e}'
        print(rta_3)
    else:
        print(num)
main()

# Solución de la guía:

"""
def apply_function(f, n):
    '''
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    '''
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():
    '''
    Función que aplica una función seleccionada por el usuario (seno, coseno, tangente, exponencial o logarítmo) a la lista de enteros desde 1 hasta n. 
    Imprime por pantalla una tabla con la secuencia de enteros y el resultado de aplicarles la función introducida.
    Parámetros:
        f: Es una cadena con la función a aplicar (sin, cos, tan, exp o log).
        n: Es un entero positivo.
    '''
    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()
"""
