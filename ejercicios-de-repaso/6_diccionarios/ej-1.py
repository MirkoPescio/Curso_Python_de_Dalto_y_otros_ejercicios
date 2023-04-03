"""
Ejercicio 1
Escribir un programa que guarde en una variable el diccionario
{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y
muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

# Mi solución:

monedas = [('Euro', '€'), ('Dollar', '$'), ('Yen', '¥')]

dict_monedas = dict(monedas)
print(dict_monedas)

ingreso_divisa = input("Ingrese el nombre de alguna divisa: ")
divisa_encontrada = {}

for moneda in dict_monedas:
    simbolo = dict_monedas.get(moneda)
    if(ingreso_divisa.capitalize() == moneda):
        divisa_encontrada[moneda] = simbolo
    
for divisa, simbolo in divisa_encontrada.items():
    if(ingreso_divisa.capitalize() == divisa):
        print(ingreso_divisa + " está en el diccionario de divisas")
        print(divisa, simbolo)
    else:
        print(ingreso_divisa + " no está en el diccionario de divisas registradas")


# Solución de la guía:

### Solución 1:

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))

### Solución 2:

monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")


