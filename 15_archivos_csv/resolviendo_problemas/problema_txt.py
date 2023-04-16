# -*- coding: utf-8 -*-
"""
Tenemos 2 listas con nombres y apellidos.

Tenemos que escribir los datos en un archivo de texto de forma óptima con
un ciclo for

"""

nombres = ["Leandro", "Adrián", "Camila", "Mariana", "Rui"]
apellidos = ["Vásquez", "Pisso", "Dalto", "Martí", "Torres"]

with open("nombres_y_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son: \n\n")
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n----------------------\n') for n,a in zip(nombres, apellidos)]



