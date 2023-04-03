"""
¿Qué es el desempaquetado de variables en Python?

Es una técnica de python (y también de otros lenguajes de programación) de
asignarle valores a variables de una forma particular.

¿Cómo puede aplicarse esa técnica? Por ejemplo crear una variable a partir de un
valor de una tupla o una lista
"""

tupla_1 = ("Iron Man", "Hulk", "Capitan América", "Thor", "Black Widow", "Ant-Man")

avenger_1, avenger_2, avenger_3, avenger_4, avenger_5, avenger_6 = tupla_1
print(avenger_1, avenger_2, avenger_3, avenger_4, avenger_5, avenger_6)
print(avenger_3)

lista_1 = ["Thanos", "Venom", "Red Skull", "Ultrón", "Rhino"]

villano_1, villano_2, villano_3, villano_4, villano_5 = lista_1
print(villano_1, villano_2, villano_3, villano_4, villano_5)
print(villano_4)







