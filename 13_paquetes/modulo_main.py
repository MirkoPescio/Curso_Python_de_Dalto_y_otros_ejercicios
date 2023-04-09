# Archivo principal del programa


## import package_1

## print(type(package_1)) # class module
## print(package_1.__path__) # me devuelve la ruta del paquete en una lista



from package_1 import saludar, consulta_curso


saludo = saludar.funcion_saludar_1
consulta = consulta_curso.funcion_consulta_del_curso
print(saludo("Mirko"))
print(consulta("Mirko"))

