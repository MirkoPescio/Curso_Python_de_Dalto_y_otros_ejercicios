"""
Crear una función que nos devuelva los números primos entre 0 y el argumento que le
pasemos
"""

# Mi solución:

def es_primo(numero):
    maximo_divisores = 2
    contador_divisores = 0
    resultado = False
    for i in range(1, numero+1):
        if(numero % i == 0):
            contador_divisores += 1
    if(contador_divisores == 2):
        resultado = True
    return resultado
        
def listar_numeros_primos(numero):
    lista_numeros_primos = []
    for u in range(numero):
        if (es_primo(u)):
            lista_numeros_primos.append(u)
    return lista_numeros_primos

def main():
    numero = int(input("Ingrese un número entero y positivo: "))
    while(numero <= 0):
        numero = int(input("Reingrese el número: "))
    lista_de_numeros_primos = listar_numeros_primos(numero)
    print(lista_de_numeros_primos)
main()


# Solución de Dalto:


def es_primo_2(num):
    for i in range(2, num-1):
        if num%i==0: return False
    return True

def primos_hasta(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if resultado == True: primos.append(i)
    return primos

resultado = primos_hasta(58)
print(resultado)

