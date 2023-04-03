# Creando diccionarios con dict()

diccionario_1 = dict(nombre = "Mirko", apellido = "Pescio")

print(diccionario_1)

"""
Es importante saber que las tuplas SI pueden ser claves de un diccionario, pero una
lista NO, ya que la lista no es 'hasheable'
La única manera de establecer a una lista como clave de un diccionario es definiendola
mediante la función frozenset()
"""

diccionario_2 = {("dato1", "dato2"): "valor1"}
print(diccionario_2)

diccionario_3 = {frozenset(["dato1", "dato2"]): "valor1"}
print(diccionario_3)


# Creando diccionarios con fromkeys()
## Dicho diccionario tiene todos sus valores en 'None' (valor nulo)

diccionario_4 = dict.fromkeys(["nombre", "apellido", "teléfono"])
print(diccionario_4)
print(diccionario_4["nombre"])
print(diccionario_4["teléfono"])

"""
También hay que saber que con fromkeys podemos iterar su primer dato
como índices-clave del diccionario creado, y su segundo dato como un
dato fijo asignado a cada uno de los índices-clave
Eso se ve mejor con el siguiente ejemplo
"""

diccionario_5 = dict.fromkeys("ABCDE", "12345")
print(diccionario_5)

diccionario_6 = dict.fromkeys(["nombre", "apellido", "teléfono"], "No sé")
### En este caso, se puede ver mejor como el primer dato es iterable
print(diccionario_6) 










