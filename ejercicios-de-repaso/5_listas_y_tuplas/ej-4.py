"""
Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor.
"""

# Mi solución:

lista_numeros_loteria = []
cantidad_numeros_loteria = int(input("Ingrese la cantidad de números ganadores de esta lotería: "))
numero = ""
contador_numeros_ingresados = 0

while(contador_numeros_ingresados < cantidad_numeros_loteria):
    numero = int(input("Ingrese un número ganador: "))
    while((numero <= 0) or (numero > 99)):
        print("Los números de la lotería pueden ir del 1 al 99")
        numero = int(input("Reingrese un número ganador: "))
    lista_numeros_loteria.append(numero)
    contador_numeros_ingresados += 1
    
lista_numeros_loteria.sort()
numeros_ganadores = "Números ganadores: "

for num in lista_numeros_loteria:
    numeros_ganadores += str(num) + ", "
    
print(numeros_ganadores)


# Solución de la guía:

"""
awarded = []
for i in range(6):
    awarded.append(int(input("Introduce un número ganador: ")))
awarded.sort()
print("Los números ganadores son " + str(awarded))
"""

