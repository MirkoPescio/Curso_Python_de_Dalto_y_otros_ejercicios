import re


text = "Reemplazando todas las vocales por asteriscos"

new_text = re.sub("[aeiou]", "*", text)

print(new_text)

