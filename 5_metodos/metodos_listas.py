lista_1 = ["Activision", "EA Sports", "Ubisoft", "Rockstar Games", "2K"]
lista_2 = ["Los Vengadores", "La Liga de la Justicia", "Los 4 Fantásticos", "X-Men"]
lista_3 = ["Spiderman", "Batman", "Wolverine", "Ironnan", "Thor", "Reed", "Rorschach"]
lista_4 = ["Venom", "El Guasón", "Harley Queen", "Bane", "Magneto", "Thanos", "Ultrón"]
lista_5 = [21, 80, 20, 2020, 2023, 455, True, False, False]


# list: éste no es un método sino una función. Sea usa para crear listas

lista_funcion_list = list(["Hola", "soy", "Dalto", 25])
print(lista_funcion_list)

# len: tampoco es un método. Cuenta la cantidad de elementos en la lista

print(len(lista_1))

# append: agrega un elemento a la lista

lista_1.append("Rocksteady")
print(lista_1)

# insert: agrega un elemento a la lista especificando el lugar a ocupar

lista_2.insert(2, "Watchmen")
print(lista_2)

# extend: agregamos varios elementos a la lista

lista_3.extend(["La Mole", "Hulk", "Capitán América", "Starfire"])
print(lista_3)

# pop: elimina un elemento de la lista por su índice

print(len(lista_4))
lista_4.pop(1) #Elimina: "El Guasón"
print(lista_4)
print(len(lista_4))

"¿Cómo hacemos para eliminar el último elemento?"

print(len(lista_3))
lista_3.pop(-1) #Elimina: "Starfire"
print(lista_3)
print(len(lista_3))

"Con -1 eliminamos el último elemento, con -2 el anteúltimo y así sucesivamente"

# remove: elimina un elemento de la lista por su valor

print(len(lista_1))
lista_1.remove("Activision")
print(lista_1)
print(len(lista_1))

# clear: elimina todos los elementos de la lista

print(len(lista_4))
lista_4.clear()
print(lista_4)
print(len(lista_4))

# sort: es un método que ordena los elementos de la lista, siempre y cuando la lista no tenga elementos de tipo String

print(lista_5)
lista_5.sort() # Los ordena de forma ascendente
print(lista_5)
lista_5.sort(reverse=True) # Los ordena de forma descendente
print(lista_5)

# reverse: invierte los elementos de CUALQUIER lista

print(lista_1)
lista_1.reverse()
print(lista_1)


