"""
Ejercicio 1
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el 
nombre tabla-n.txt la tabla de multiplicar de ese número, done n es el número introducido.
"""

# Mi solución:

def funcion_ingresar_numero():
    numero = int(input("Ingrese un número entero entre 1 y 10: "))
    while((numero < 1) or (numero > 10)):
        numero = int(input("Reingrese un numero ENTRE 1 Y 10: "))
    return numero

def funcion_respectiva_tabla_de_multiplicar(numero):
    lista_numero_tabla = []
    numero_resultado = ""
    for i in range(1, 10+1):
        numero_resultado = numero * i
        lista_numero_tabla.append(numero_resultado)
    return lista_numero_tabla

def main():
    tabla_del_numero = funcion_ingresar_numero()
    lista_numeros_de_la_tabla = funcion_respectiva_tabla_de_multiplicar(tabla_del_numero)
    print(f"Generando tabla del {tabla_del_numero} en un archivo de texto txt...")
    with open(f"./ejercicios-de-repaso/9_ficheros/tabla-{tabla_del_numero}.txt", "w", encoding="UTF-8") as archivo:
        for numero in lista_numeros_de_la_tabla:
            archivo.writelines([f"{numero}\n"])
main()

# Solución de la guía:

## Solución 1:

"""
n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
f = open(nombre_fichero, 'w')
for i in range(1, 11):
    f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
f.close()
"""

## Solución 2:

"""
n = int(input('Introduce un número entero entre 1 y 10: '))
nombre_fichero = 'tabla-' + str(n) + '.txt'
with open(nombre_fichero, 'w') as f:
    for i in range(1, 11):
        f.write(str(n) + ' x ' + str(i) + ' = ' + str(n * i) + '\n')
"""
