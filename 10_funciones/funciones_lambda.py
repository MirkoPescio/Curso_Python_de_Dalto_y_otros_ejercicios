"""
Las funciones lambda son funciones anónimas que pueden definirse en sólo una línea de
código. Dichas funciones son almacenadas en variables
"""

multiplicar_por_dos = lambda x : x * 2

print(multiplicar_por_dos(5)) # RTA: 10
print(multiplicar_por_dos(25)) # RTA: 50

"Hay que saber que no son aptas para definir funciones que requieren mas de 1 instrucción"

# Usando Filter en una función común:

lista_numeros = [1, 2, 4, 5, 7, 8, 9, 11, 13, 14, 15, 17, 19, 20]

def es_par(num):
    rta = False
    if(num % 2 == 0):
        rta = True
    return rta

numeros_pares = filter(es_par, lista_numeros)

print(numeros_pares) # Nos devuelve un elemento de tipo object
print(list(numeros_pares)) # Nos devuelve la lista filtrada (los números pares)

print("\n")

# Haciendo lo mismo pero con lambda:


numeros_pares_lambda = filter(lambda x : x % 2 == 0, lista_numeros)

print(numeros_pares_lambda)
print(list(numeros_pares_lambda))



