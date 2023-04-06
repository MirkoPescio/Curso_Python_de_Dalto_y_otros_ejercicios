"""
Ejercicio 2
Escribir una función a la que se le pase una cadena <nombre> y muestre
por pantalla el saludo ¡hola <nombre>!.
"""

# Mi solución:

def saludo(nombre):
    texto_saludo = f'¡Hola {nombre}!'
    return texto_saludo

def main():
    nombre = input("Ingrese su nombre: ")
    respuesta_saludo = saludo(nombre)
    print(respuesta_saludo)
main()


# Solución de la guía:

def greet(nombre):
    """Función que muestra un saludo por pantalla.
    Parámetros
    nombre: Nombre del usuario
    Devuelve el saludo ¡Hola nombre!.
    """
    print('¡Hola ' + nombre +'!')
    return

greet('Alf')
greet('Python')

