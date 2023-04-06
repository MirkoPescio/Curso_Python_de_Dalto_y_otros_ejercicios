"""
Ejercicio 4
Escribir una función que calcule el total de una factura tras aplicarle
el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a
aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle
el porcentaje de IVA, deberá aplicar un 21%.
"""

# Mi solución:

def ingreso_precio_producto():
    precio_producto = float(input("Ingrese el precio del producto: "))
    while(precio_producto <= 0):
        precio_producto = float(input("Reingrese el precio del producto: "))
    return precio_producto

def ingreso_IVA():
    porcentaje_IVA = float(input("Ingrese el porcentaje del IVA (0 <= IVA <= 1): "))
    while(porcentaje_IVA <= 0 or porcentaje_IVA > 1):
        porcentaje_IVA = float(input("Reingrese el porcentaje del IVA (0 <= IVA <= 1): "))
    return porcentaje_IVA

def precio_final(precio_producto, porcentaje_IVA=0.21):
    IVA_del_producto = precio_producto * porcentaje_IVA
    calculo_precio_final = precio_producto + IVA_del_producto
    return calculo_precio_final

def main():
    precio_producto = ingreso_precio_producto()
    IVA = ingreso_IVA()
    precio_final_1 = precio_final(precio_producto, IVA)
    precio_final_2 = precio_final(precio_producto)
    print(precio_final_1)
    print(precio_final_2)
main()

print("\n")

# Solución de la guía:

def invoice(amount, vat=21):
    """Función de aplica el IVA a una factura.
    Parametros
    amount: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA. 
    """
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))

