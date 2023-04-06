"""
Ejercicio 5
Escribir una función que calcule el área de un círculo y otra que calcule el
volumen de un cilindro usando la primera función.
"""

# Mi solución:

def area_circulo(radio):
    pi = 3.1416
    area = pi * (radio**2)
    return area

def volumen_cilindro(superficie_circulo, altura):
    volumen = superficie_circulo * altura
    return volumen

def main():
    radio_circulo = float(input("Ingrese el radio del círculo: "))
    while(radio_circulo <= 0):
        radio_circulo = float(input("Reingrese el radio del circulo: "))
    altura_cilindro = float(input("Ingrese la altura del cilindro: "))
    while(altura_cilindro <= 0):
        altura_cilindro = float(input("Reingrese la altura del cilindro: "))
    superficie = area_circulo(radio_circulo)
    volumen = volumen_cilindro(superficie, altura_cilindro)
    respuesta_area = f'El área del círculo en el cilindro es de {superficie} u**2'
    respuesta_volumen = f'El volumen del cilindro es de {volumen} u**2'
    print(respuesta_area)
    print(respuesta_volumen)
main()


# Solución de la guía:

def circle_area(radius):
    """Función que calcula el area de un círculo.
    Parámetros
    radius: Es el radio del círculo.
    Devuelve el área del círculo de radio radius. 
    """
    pi = 3.1415
    return pi*radius**2

def cilinder_volume(radius, high):
    """Función que calcula el volumen de un cilindro.
    Parámetros
    radius: Es el radio de la base del cilindro.
    high: Es la altura del cilindro.
    Devuelve el volumen del clindro de radio radius y altura high.
    """
    return circle_area(radius)*high

print(cilinder_volume(3,5))


