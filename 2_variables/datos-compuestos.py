# Listas
# Las listas se pueden modificar

lista_1 = ["Mirko Pescio", "MirkoIP99", True, 1.71]
print(lista_1)  # Me imprime todo el array
print(lista_1[3]) # Me imprime ==> 1.71

# Tuplas
# Las tuplas no se pueden modificar

tupla_1 = ("Mirko Pescio", "MirkoIP99", True, 1.71)
print(tupla_1)
print(tupla_1[0])

# Set (o conjunto)
# Otro tipo de dato compuesto similar a las listas

set_1 = {"Lucas Dalto", "Soy Dalto", True, 1.85}
set_2 = {"jajajajaja Máquina te jodí"}
print(set_1)
print(set_2)
# Algo fundamental de los sets es que no se permiten repetir valores
# Por ejemplo {"Lucas Dalto", "Soy Dalto", True, 1.85, "YouTube", "Soy Dalto", [], "String"}
# En este caso va a dar un error ya que "Soy Dalto" está repetido en el set
# Tampoco se puede acceder a elementos por índice en los sets


"Último tipo de dato complejo ==> los diccionarios"
# La estructura de un diccinario es {'key': value}
# Igual a los JSON en Javascript

dict_1 = {}
dict_2 = {
    'nombre': 'Lucas Dalto',
    'canal_youtube': 'Soy Dalto',
    '¿Programa?': True,
    'altura': 1.84,
    'dato_repetido': 'Soy Dalto'
}

print(dict_2['nombre']) # Me imprime: Lucas Dalto