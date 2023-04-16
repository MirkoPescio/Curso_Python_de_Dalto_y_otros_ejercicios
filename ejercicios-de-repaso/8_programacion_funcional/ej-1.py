"""
Ejercicio 1
Escribir una función que aplique un descuento a un precio y otra que aplique el 
IVA a un precio. Escribir una tercera función que reciba un diccionario con los 
precios y porcentajes de una cesta de la compra, y una de las funciones anteriores,
y utilice la función pasada para aplicar los descuentos o el IVA a los productos 
de la cesta y devolver el precio final de la cesta.
"""

# Mi solución:

def aplicar_descuento(precio_original):
    porcentaje_descuento = float(input("Ingrese el porcentaje de descuento (0 a 1): "))
    while((porcentaje_descuento <= 0) or (porcentaje_descuento >=1)):
        porcentaje_descuento = float(input("Reingrese el porcentaje de descuento (0 a 1): "))
    precio_con_descuento = precio_original - (precio_original * porcentaje_descuento)
    return (porcentaje_descuento, precio_con_descuento)


def aplicar_IVA(precio_original):
    porcentaje_IVA = float(input("Ingrese el porcentaje de IVA (0 a 1): "))
    while((porcentaje_IVA <= 0) or (porcentaje_IVA >= 1)):
        porcentaje_IVA = float(input("Reingrese el porcentaje de IVA (0 a 1): "))
    precio_con_IVA = precio_original + (precio_original * porcentaje_IVA)
    return (porcentaje_IVA, precio_con_IVA)


def main():
    precio_original = float(input("Ingrese el precio original de un producto: "))
    while(precio_original <= 0):
        precio_original = float(input("Reingrese el precio original del producto: "))
    porcentaje_descuento, con_descuento = aplicar_descuento(precio_original)
    rta_1 = f'El producto cuyo precio es de ${precio_original} con un {porcentaje_descuento * 100}% de descuento, va a tener un valor final de ${con_descuento}'
    porcentaje_IVA, con_IVA = aplicar_IVA(precio_original)
    rta_2 = f'El producto cuyo precio es de ${precio_original} con un {porcentaje_IVA * 100}% de IVA, va a tener un valor final de ${con_IVA}'
    print(rta_1)
    print(rta_2)
main()
    
# Solución de la guía:

"""
def apply_discount(price, discount):
    '''
    Función que aplica un descuento a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el descuento.
        discount: Es el porcentaje a descontar.
    Devuelve:
        El precio final tras aplicar el descuento.
    '''
    return price - price * discount / 100
    
def apply_IVA(price, percentage):
    '''
    Función que aplica un IVA a una cantidad.
    Parámetros:
        price: Es un valor real con el precio al que aplicar el IVA.
        percentage: Es el porcentaje del IVA a aplicar.
    Devuelve:
        El precio final tras aplicar el IVA.
    '''
    return price + price * percentage / 100

def price_basket(basket, function):
    '''
    Función que calcula el precio de una cesta de la compra una vez aplicada una función a los precios iniciales.
    Parámetros:
        basket: Es un diccionario formado por pares precio:descuento.
        function: Es una función que toma dos valores reales y devuelve otro. Normalmente para aplicar descuentos o IVA.
    Devuelve:
        El precio final de la cesta de la compra una vez aplicada la función sobre los precios iniciales.
    '''
    total = 0
    for price, discount in basket.items():
        total += function(price, discount)
    return total
"""
