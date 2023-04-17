"""
Ejercicio 5
Escribir una función que reciba una frase y devuelva un diccionario con las 
palabras que contiene y su longitud.
"""

# Mi solución

def diccionario_palabras_longitud(frase):
    lista_de_palabras = frase.split(" ")
    diccionario = {}
    for palabra in lista_de_palabras:
        diccionario[palabra] = len(palabra)
    return diccionario

def main():
    frase = input("Ingrese un texto: ")
    dicc_palabras_longitud = diccionario_palabras_longitud(frase)
    print(dicc_palabras_longitud)
main()

print("\n")

# Solución de la guía:

## Solución 1:

def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    words = sentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(length_words('Welcome to Python'))
print("\n")

## Solución 2:

def length_words(sentence):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras que contiene y su longitud.
    Parámetros:
        sentence: Es una cadena de caracteres con una frase.
    Devuelve:
        Un diccionario con pares palabra:longitud donde palabra son las palabras que contiene la frase sentence.
    '''
    return {word:len(word) for word in sentence.split()}

print(length_words('Welcome to Python'))
