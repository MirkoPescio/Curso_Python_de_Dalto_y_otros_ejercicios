"""
Ejercicio 4
Escribir un programa que acceda a un fichero de internet mediante su url y muestre por 
pantalla el número de palabras que contiene.
"""

from urllib import request

### URL DE EJEMPLO: https://example-files.online-convert.com/document/txt/example.txt

# Mi solución:

def funcion_leer_fichero(fichero_url):
    try:
        with request.urlopen(fichero_url) as archivo:
            texto = archivo.read()
    except:
        print("No se encontró el archivo con la url ingresada")
    return texto.decode('utf-8')

def listar_palabras_fichero(texto):
    lista_palabras = texto.split(" ")
    return lista_palabras

def contar_palabras_texto(lista_palabras):
    cantidad_palabras = len(lista_palabras)
    return cantidad_palabras

def main():
    fichero_url = input("Ingrese la URL del fichero a leer: ")
    leer_fichero = funcion_leer_fichero(fichero_url)
    lista_de_palabras = listar_palabras_fichero(leer_fichero)
    cantidad_palabras_texto = contar_palabras_texto(lista_de_palabras)
    rta = f'La cantidad de palabras en el texto del fichero ingresado es de {cantidad_palabras_texto} palabras'
    print(rta)
main()

# Solución de la guía:

## Solución 1: 

def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        f = request.urlopen(url)
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        contenido = f.read()
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))

## Solución 2:

def contar_palabras(url):
    '''
    Función que recibe recibe la url de un fichero de texto y devuelve el número de palabras que contiene.
    Parámetros:
        url: Es una cadena con la url del fichero de texto.
    Devuelve:
        El número de palabras que contiene el fichero de texto daro por la url.
    '''
    from urllib import request
    from urllib.error import URLError
    try:
        with request.urlopen(url) as f:
            contenido = f.read()
    except URLError:
        return('¡La url ' + url + ' no existe!')
    else:
        return len(contenido.split())

print(contar_palabras('https://www.gutenberg.org/files/2000/2000-0.txt'))
print(contar_palabras('https://no-existe.txt'))
