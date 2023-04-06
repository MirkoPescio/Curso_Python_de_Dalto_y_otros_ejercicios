"""
Ejercicio 9
Escribir una función que calcule el máximo común divisor de dos números y otra
que calcule el mínimo común múltiplo.
"""

# Mi solución:

"Para ambas funciones los parámetros van a ser los números"

def ingreso_2_numeros():
    num_1 = int(input("Ingrese un número entero positivo: "))
    while(num_1 <= 0):
        num_1 = int(input("Reingrese el número: "))
    num_2 = int(input("Ingrese otro número entero positivo: "))
    while(num_2 <= 0):
        num_2 = int(input("Reingrese el número: "))
    return num_1, num_2

def maximo_comun_divisor(num1, num2):
    mcd = 1
    if (num1 % num2 == 0):
        return num2
    for i in range(int(num2/2), 0, -1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            mcd = i
            break
    return mcd

def minimo_comun_multiplo(num1, num2):
    num_mas_alto = max(num1, num2)
    """
    Definimos el número más alto entre ambos ya que es a partir de este
    en el que empieza a contarse los múltiplos
    """
    while True:
        if ((num_mas_alto % num1 == 0) and (num_mas_alto % num2 == 0)): 
            return num_mas_alto
        num_mas_alto += 1

def main():
    tupla_numeros = ingreso_2_numeros()
    numero_1 = tupla_numeros[0]
    numero_2 = tupla_numeros[1]
    MCD = maximo_comun_divisor(numero_1, numero_2)
    mcm = minimo_comun_multiplo(numero_1, numero_2)
    resultante_MCD = f'El máximo común divisor entre {numero_1} y {numero_2} es {MCD}'
    resultante_mcm = f'El mínimo común múltiplo entre {numero_1} y {numero_2} es {mcm}'
    print(resultante_MCD)
    print(resultante_mcm)
main()

# Solución de la guía:

def mcd(n, m):
    """Función que calcula el máximo común divisor de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El máximo común divisor de n y m.
    """
    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

def mcm(n, m):
    """Función que calcula el mínimo común múltiplo de dos números.
    Parámetros:
        - n: Es un número entero.
        - m: Es un número entero.
    Devuelve:
        El mínimo común múltiplo de n y m.
    """
    if n > m:
        greater = n
    else:
        greater = m
    while (greater % n != 0) or (greater % m != 0):
        greater += 1
    return greater

print(mcd(24,36))
print(mcm(24,36))



