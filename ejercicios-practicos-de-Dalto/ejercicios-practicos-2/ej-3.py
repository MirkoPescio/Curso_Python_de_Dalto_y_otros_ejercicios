"""
Realizar un listado de números (similar al ejercicio anterior) con la serie de
Fibonacci
"""

# Mi solución:


def calculo_serie_fibonacci(numero_inicial, cantidad_de_sucesiones):
    lista_fibonacci = []
    lista_fibonacci.append(numero_inicial)
    calculo = 0
    for i in range(cantidad_de_sucesiones):
        calculo = lista_fibonacci[i] + lista_fibonacci[i-1]
        lista_fibonacci.append(calculo)
    return lista_fibonacci

def main():
    numero_inicial = int(input("Ingrese un número entero y positivo (inicio de la serie Fibonacci): "))
    while(numero_inicial <= 0):
        numero = int(input("Reingrese un número entero y positivo: "))
    cantidad_de_sucesiones = int(input("Ingrese un número entero y positivo (cantidad de repeticiones de la serie Fibonacci): "))
    while(cantidad_de_sucesiones <= 0):
        cantidad_de_sucesiones = int(input("Reingrese un número entero y positivo: "))
    listado_fibonacci = calculo_serie_fibonacci(numero_inicial, cantidad_de_sucesiones)
    print(listado_fibonacci)
main()


# Solución de Dalto:

def fibonacci(num):
    a, b = 0, 1
    fibonacci_lista = [0]
    for i in range(num):
        if b > num: return fibonacci_lista
        else:
            fibonacci_lista.append(b)
            a, b = b, a+b

resultado_1 = fibonacci(34)
resultado_2 = fibonacci(35)
resultado_3 = fibonacci(400)
print(resultado_1)
print(resultado_2)
print(resultado_3)

