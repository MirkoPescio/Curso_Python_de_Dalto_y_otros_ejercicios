"""
Ejercicio 10
Escribir una función que convierta un número decimal en binario y otra que convierta
un número binario en decimal.
"""

# Mi solución:

def conversion_decimal_a_binario(num):
    num_convertido = bin(num)
    return num_convertido

def conversion_binario_a_decimal(num):
    numero_binario = conversion_decimal_a_binario(num)
    num_convertido = int(str(numero_binario), 2)
    return num_convertido

def main():
    numero = int(input("Ingrese un número: "))
    de_decimal_a_binario = conversion_decimal_a_binario(numero)
    de_binario_a_decimal = conversion_binario_a_decimal(numero)
    resultante_1 = de_decimal_a_binario
    resultante_2 = de_binario_a_decimal
    print(resultante_1)
    print(resultante_2)
main() 

print("\n")

# Solución de la guía:

def to_decimal(n):
    """Función que convierte un número binario en decimal.
    Parámetros:
        - n: Es una cadena de ceros y unos.
    Devuelve:
        El número decimal correspondiente a n.
    """
    n = list(n)
    n.reverse()
    decimal = 0
    for i in range(len(n)):
        decimal += int(n[i]) * 2 ** i
    return decimal

def to_binary(n):
    """Función que convierte un número decimal en binario.
    Parámetros:
        - n: Es un número entero.
    Devuelve:
        El número binario correspondiente a n.
    """
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)

print(to_decimal('10110'))
print(to_binary(22))
print(to_decimal(to_binary(22)))
print(to_binary(to_decimal('10110')))

