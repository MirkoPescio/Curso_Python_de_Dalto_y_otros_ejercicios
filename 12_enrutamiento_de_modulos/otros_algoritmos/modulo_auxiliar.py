"""
Incorporamos funciones en una ruta que se encuentra en otro nivel
En este caso sería ../mis_algoritmos/algoritmos_1.py
"""

import sys

sys.path.append(r"C:\Users\Mirko\Desktop\curso_de_Dalto\12_enrutamiento_de_modulos\mis_algoritmos")

import algoritmos_1 as mi_saludo

print(mi_saludo.saludar("Mirko"))
