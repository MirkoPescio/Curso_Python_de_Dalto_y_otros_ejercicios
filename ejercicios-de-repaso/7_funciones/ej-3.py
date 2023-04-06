"""
Ejercicio 3
Escribir una función que reciba un número entero positivo y devuelva su
factorial.
"""

# Mi solución:

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

def ingreso():
    numero = int(input("Ingrese un número entero y positivo: "))
    while(numero <= 0):
        numero = int(input("Reingrese el número: "))
    return numero

def main():
    numero = ingreso()
    calculo_factorial = factorial(numero)
    respuesta_final = f'El factorial del número {numero} es igual a {calculo_factorial}'
    print(respuesta_final)
main()


# Solución de la guía:

def factorial_2(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    tmp = 1
    for i in range(n):
        tmp *= i+1
    return tmp

print(factorial_2(4))
print(factorial_2(20))


