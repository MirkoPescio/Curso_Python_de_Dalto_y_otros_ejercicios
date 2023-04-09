
def saludar(nombre):
    saludo = f'¡Hola {nombre}! ¿Como estás?'
    return saludo

def saludar_raro(nombre):
    saludo_raro = f'¡K onda {nombre}! Espero que estés nashe, anasheli anasheiii'
    return saludo_raro

def main_saludar():
    nombre = input("Ingrese su nombre: ")
    funcion_saludar = saludar(nombre)
    return funcion_saludar

def main_saludar_raro():
    nombre = input("Ingrese su nombre: ")
    funcion_saludar_raro = saludar_raro(nombre)
    return funcion_saludar_raro

