

def saludar(nombre):
    saludo = f'¡Hola {nombre}! ¿¡Como estás!?'
    return saludo


def main_saludar():
    nombre_ingreso = input("Ingrese su nombre: ")
    saludo = saludar(nombre_ingreso)
    return saludo

