import re


text = "Este es un ejemplo de una página web: https://www.example.com y/o también puede visitarnos en https://www.example.org"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)
