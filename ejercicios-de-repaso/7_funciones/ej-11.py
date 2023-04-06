"""
Ejercicio 11
Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario
con cada palabra que contiene y su frecuencia.
Escribir otra función que reciba el diccionario generado con la función anterior
y devuelva una tupla con la palabra más repetida y su frecuencia.
"""

# Mi solución:

def almacenar_frecuencia_palabras(cadena):
    diccionario_frecuencia_palabras = {}
    simbolos = ",;.:\¡!¿?"
    for caracter in simbolos:
        cadena = cadena.replace(caracter, "")
    tupla_palabras = cadena.split(" ")
    for palabra in tupla_palabras:
        if (palabra in diccionario_frecuencia_palabras):
            diccionario_frecuencia_palabras[palabra] += 1
        else:
            diccionario_frecuencia_palabras[palabra] = 1
    return diccionario_frecuencia_palabras


def valor_maxima_frecuencia(cadena):
    diccionario_palabras = almacenar_frecuencia_palabras(cadena)
    frecuencia_maxima = 0
    for palabra, frecuencia in diccionario_palabras.items():
        if (frecuencia_maxima < frecuencia):
            frecuencia_maxima = frecuencia
    return frecuencia_maxima
    
def obtener_palabra_mas_frecuente(cadena):
    diccionario_palabras = almacenar_frecuencia_palabras(cadena)
    valor_frecuencia_maxima = valor_maxima_frecuencia(cadena)
    lista_final = []
    for palabra, frecuencia in diccionario_palabras.items():
        if (frecuencia == valor_frecuencia_maxima):
            lista_final.append((palabra, frecuencia))
    return lista_final

def main():
    cadena = input("Ingrese un texto: ")
    diccionario_palabras = almacenar_frecuencia_palabras(cadena)
    lista_palabras_mas_frecuentes = obtener_palabra_mas_frecuente(cadena)
    print(diccionario_palabras)
    resultante_frecuencia = f'La/las palabra/s más frecuente/s con su/s respectivo/s valor/es es/son {lista_palabras_mas_frecuentes}'
    print(resultante_frecuencia)
main()

# Solución de la guía:

def count_words(text):
    """Función que cuenta el número de veces que aparece cada palabra en un texto.
    Parámetros:
        - text: Es una cadena de caracteres.
    Devuelve: 
        Un diccionario con pares palabra:frecuencia con las palabras contenidas en el texto y su frecuencia.
    """
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words

def most_repeated(words):
    max_word = ''
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq

text = 'Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera'
print(count_words(text))
print(most_repeated(count_words(text)))

