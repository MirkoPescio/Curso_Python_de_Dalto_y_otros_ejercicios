"""
Ejercicio 10
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g
y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.
"""

# Mi solución:
PESO_PAYASO = 112
PESO_MUNECA = 75 # Ambos son pesos en gramos

cant_payasos = int(input("Ingrese la cantidad de payasos de este pedido: "))

while cant_payasos <= 0:
    cant_payasos = int(input("Reingrese una cantidad válida de payasos: "))

cant_munecas = int(input("Ingrese la cantidad de muñecas de este pedido: "))

while cant_munecas <= 0:
    cant_munecas = int(input("Reingrese una cantidad válida de muñecas: "))

peso_total_payasos = cant_payasos * PESO_PAYASO
peso_total_munecas = cant_munecas * PESO_MUNECA

peso_total_pedido = peso_total_payasos + peso_total_munecas
print("El peso total del pedido es de " + str(peso_total_pedido / 1000) + " KG")

# Solución de la página web:

"""
peso_payaso = 112
peso_muñeca = 75
payasos = int(input("Introduce el número de payasos a enviar: "))
muñecas = int(input("Introduce el número de muñecas a enviar: "))
peso_total = peso_payaso * payasos + peso_muñeca * muñecas
print("El peso total del paquete es " + str(peso_total))
"""

