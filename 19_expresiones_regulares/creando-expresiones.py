import re


# Detectando un número de Buenos Aires y ocultandolo
texto = "Hola Pedro, mi número es: +54 11-4321-4321"

pattern = r'\+\d{2}\s\d{2}-\d{4}-\d{4}'

reemplazo = re.sub(pattern, "(Número oculto)", texto)

print(reemplazo)
