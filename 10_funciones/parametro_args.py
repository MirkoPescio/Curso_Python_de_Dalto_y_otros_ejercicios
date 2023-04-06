# Forma no óptima de sumar valores

lista_numeros_1 = [4, 6, 19, 37, 40]

def suma_1(lista):
    numeros_sumados = 0
    for numero in lista:
        numeros_sumados += numero
    return numeros_sumados

resultado_1 = suma_1(lista_numeros_1)
print(resultado_1)

# Forma óptima de sumar valores:
## Usamos el parámetro args:

def suma_2(nombre, *numeros): # Aclaración el parametro args * tiene que usarse al final
    suma = sum(numeros)
    return f"Hola {nombre}, la suma de tus números es: {suma}"

nombre = input("Ingrese su nombre: ")
resultado_2 = suma_2(nombre, 4, 6, 19, 37, 40)
print(resultado_2)

## Otra forma de aplicarlo:

def suma_3(numeros):
    return sum([*numeros])

resultado_3 = suma_3([4, 6, 19, 37, 40])
print(resultado_3)







