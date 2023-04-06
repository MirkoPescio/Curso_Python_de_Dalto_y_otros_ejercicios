
# Ejemplo de función simple:
def saludar():
    nombre = input("Ingrese su nombre de usuario: ")
    print(f'Hola {nombre}, como estás?')
    
saludar()

# Ejemplo de función con parámetros:

def saludar_2(curso):
    print(f'Bienvenido/a al curso de {curso}')
    
curso = input("Ingrese el nombre del curso: ")

saludar_2(curso)

def eleccion_auto(nombre, marca):
    marca = marca.lower()
    if (marca == "volkswagen"):
        auto = "Volkswagen Virtus"
    elif (marca == "ford"):
        auto = "Ford Fiesta"
    elif (marca == "fiat"):
        auto = "Fiat Cronos"
    elif (marca == "audi"):
        auto == "Audi R8"
    elif (marca == "peugeot"):
        auto = "Peugeot 208"
    else:
        auto = "Tesla"
    
    print(f'Hola {nombre}, en su próximo exámen de manejo va a usar un {auto}')
    
nombre = input("Ingrese su nombre: ")
marca = input("Ingrese una marca de autos: ")

eleccion_auto(nombre, marca)


# Crear una función que nos retorne valores:

def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña
    

contraseña_1 = crear_contraseña_random(53)
contraseña_2 = crear_contraseña_random(1)
contraseña_3 = crear_contraseña_random(100)
print(contraseña_1)
print(contraseña_2)
print(contraseña_3)


