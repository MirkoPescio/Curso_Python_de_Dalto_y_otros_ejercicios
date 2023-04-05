lista_1 = [4, 5, 19, 86, 50, 24, 36]
tupla_1 = (20, 1, 203, 1024, 1000, 599)

# La función max() nos busca el valor más alto de un conjunto
## Puede aplicarse para listas, tuplas, set

resultado_max_1 = max(lista_1)
resultado_max_2 = max(tupla_1)
print(resultado_max_1)
print(resultado_max_2)
print("\n")

# En cambio min() es para encontrar el valor más bajo

resultado_min_1 = min(lista_1)
resultado_min_2 = min(tupla_1)
print(resultado_min_1)
print(resultado_min_2)
print("\n")

# Redondear decimales

numero_aleatorio_1 = float(input("Ingrese un número con decimales: "))

resultado_redondeo_3decimales = round(numero_aleatorio_1, 3)
resultado_redondeo_5decimales = round(numero_aleatorio_1, 5)
print(resultado_redondeo_3decimales)
print(resultado_redondeo_5decimales)
print("\n")

# Función bool()
## Retorna False ==> 0, vacío, False, None
## Retorna True ==> distinto a 0, True, cadena de texto, datos no vacíos

dato_1 = 0
dato_2 = ()
dato_3 = []
dato_4 = False
dato_5 = None

resultado_bool_dato_1 = bool(dato_1)
resultado_bool_dato_2 = bool(dato_2)
resultado_bool_dato_3 = bool(dato_3)
resultado_bool_dato_4 = bool(dato_4)
resultado_bool_dato_5 = bool(dato_5)
"Para todos los resultados anteriores nos devuelve False"

print(resultado_bool_dato_1)
print(resultado_bool_dato_2)
print(resultado_bool_dato_3)
print(resultado_bool_dato_4)
print(resultado_bool_dato_5)
print("\n")

dato_6 = 17
dato_7 = True
dato_8 = "Cadena de texto cualquiera"
dato_9 = ("Batman", "Superman", "Wonder Woman", "Green Lantern", "Green Arrow")
dato_10 = ["Darkseid", "Zod", "Doomsday", "Joker", "Bane", "Lex Luthor"]

resultado_bool_dato_6 = bool(dato_6)
resultado_bool_dato_7 = bool(dato_7)
resultado_bool_dato_8 = bool(dato_8)
resultado_bool_dato_9 = bool(dato_9)
resultado_bool_dato_10 = bool(dato_10)
"Para todos los resultados anteriores nos devuelve True"

print(resultado_bool_dato_6)
print(resultado_bool_dato_7)
print(resultado_bool_dato_8)
print(resultado_bool_dato_9)
print(resultado_bool_dato_10)
print("\n")

# all() retorna True si todos los valores son verdaderos
### Solamente se puede aplicar a datos iterables

dato_11 = ("Avengers", 100, True, [250, 255]) # True
dato_12 = ("Justice League", [], -1) # False (lista vacía)
dato_13 = [False, 124, ("Batman", "Superman")] # False (hay un False)
dato_14 = [True, -20, ("Deathstroke", "Catwoman"), "2023"] # True

resultado_bool_dato_11 = all(dato_11)
resultado_bool_dato_12 = all(dato_12)
resultado_bool_dato_13 = all(dato_13)
resultado_bool_dato_14 = all(dato_14)

print(resultado_bool_dato_11)
print(resultado_bool_dato_12)
print(resultado_bool_dato_13)
print(resultado_bool_dato_14)
print("\n")


