import re


texto = '''Hola maestro, esta es la cadena 1
Esta es la segunda línea de texto
Y Esta es la final definitiva, capitán'''

# Haciendo una búsqueda simple:
resultado1 = re.findall("Esta", texto)

# \d -> busca dígitos numéricos del 0 - 9
resultado2 = re.findall(r"\d", texto)

# \D -> busca TODO MENOS dígitos númericos
resultado3 = re.findall(r"\D", texto)

# \w -> busca caracteres alfanuméricos [a-z A-Z 0-9 _]
resultado4 = re.findall(r"\w", texto)

# \W -> busca TODO MENOS caracteres alfanuméricos
resultado5 = re.findall(r"\W", texto)

# \s -> busca espacios en blanco -> espacios, tabs, saltos de línea
resultado6 = re.findall(r"\s", texto)

# \S -> busca TODO MENOS espacios en blanco
resultado7 = re.findall(r"\S", texto)

# \n -> busca saltos en línea
resultado8 = re.findall(r"\n", texto)

# . -> busca TODO MENOS saltos en línea
resultado9 = re.findall(r".", texto)

print(resultado1) #['Esta', 'Esta']
print("\n")

print(resultado2) #['1'] 
print("\n")

print(resultado3) #(Devuelve todo menos dígitos numéricos)
print("\n")

print(resultado4)
print("\n")

print(resultado5)
print("\n")

print(resultado6)
print("\n")

print(resultado7)
print("\n")

print(resultado8)
print("\n")

print(resultado9)
print("\n")

