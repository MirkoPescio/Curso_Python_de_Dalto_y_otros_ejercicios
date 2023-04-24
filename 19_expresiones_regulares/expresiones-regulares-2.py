import re


texto = '''Hola maestro, esta es la cadena 1. Y es la primer línea del texto
Esta es la segunda línea de texto
Tirando algunos números: 45, 128, 1000, 62, 18, 2 y 54127
Y Esta es la final definitiva, capitán.'''


#\ -> cancelamos caracteres especiales
resultado1 = re.findall(r"\.", texto)

# Armando una cadena que busque un número, seguido de un punto y un espacio
resultado2 = re.findall(r"\d\.\s", texto)

# Buscando el principio de una línea
# ^ -> busca el comienzo de una línea (buscando 'hola' al principio de una línea)
resultado3 = re.findall(r"^Hola", texto)

# flags=re.M activa la multilínea
resultado4 = re.findall(r'^Esta', texto, flags=re.M)

# $ -> busca el final de una línea
resultado5 = re.findall(r'texto$', texto, flags=re.M)

# {n} -> busca n cantidad de veces el valor de la izquierda
resultado6 = re.findall(r'\d{3}', texto)

# {n,m} -> al menos n, como máximo m
resultado7 = re.findall(r'\d{1,4}', texto)
# No se refiere a la cantidad de soluciones, sino a la cantidad de caracteres en cada una de las coincidencias

# | -> busca una cosa o la otra
resultado8 = re.findall(r'\d{1,4}|Hola', texto)


print(resultado1) # Y me devuelve todos los puntos del texto
print("\n")

print(resultado2)
print("\n")

print(resultado3)
print("\n")

print(resultado4)
print("\n")

print(resultado5)
print("\n")

print(resultado6) #['128', '100', '541']
print("\n")

print(resultado7) #['1', '45', '128', '1000', '62', '18', '2', '5412', '7']
print("\n")

print(resultado8)
print("\n")

