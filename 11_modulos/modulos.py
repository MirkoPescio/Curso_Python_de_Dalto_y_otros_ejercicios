import modulo_saludar

"""
Algo muy importante a saber:
   Una vez que importamos las funciones de un módulo, dichas funciones se almacenan
   en un objeto, con lo cual, para usarlas las llamamos como un método de ese objeto
"""

objecto_modulo_saludar = modulo_saludar.main_saludar()


print(type(modulo_saludar))
