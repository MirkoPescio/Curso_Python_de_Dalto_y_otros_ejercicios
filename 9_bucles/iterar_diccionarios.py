diccionario_1 = {
    "nombre": "Mirko",
    "apellido": "Pescio",
    "teléfono": "11-5806-9634"
}

# Recorremos el diccionario: diccionario_1

## Imprimimos por pantalla las claves del diccionario:

for key in diccionario_1:
    print(key)
    
## Imprimimos por pantalla los pares clave-valor del diccionario:

for par in diccionario_1.items():
    print(par) # Esto nos devuelve tuplas con cada par clave-valor
    
print("\n")

for datos in diccionario_1.items():
    key = datos[0]
    value = datos[1]
    print(f'La clave es: {key} y su respectivo valor es: {value}')
    
print("\n")

for clave, valor in diccionario_1.items():
    print(clave)
    print(valor)
    





