def frase(marca, auto, año):
    return f'En nuestra base de datos figura que tiene un {marca} {auto} del año {año}'

frase_resultante = frase(marca="Volkswagen", auto="Gol", año="2019")
print(frase_resultante)

# También podemos cambiar valores a parámetros predeterminados:

def frase_2(nombre, auto="Volkswagen Amarok"):
    return f'Hola {nombre}, tu auto es un {auto}'

frase_2_resultante_1 = frase_2("Mirko", auto="Volkswagen Polo")
frase_2_resultante_2 = frase_2("Dalto", "Renault Duster")
frase_2_resultante_3 = frase_2("Damián", "Chevrolet Spin")
print(frase_2_resultante_1)
print(frase_2_resultante_2)
print(frase_2_resultante_3)

