"""
Suponiendo que cada persona en promedio 2 palabras por segundo

A) Pedirle al usuario que diga cualquier texto real y:
   * Calcular cuanto tardaría en decir esa frase
   * Cuantas palabras fueron las que dijo
   
B) Si tarda más de 1 minuto, mostrarle por pantalla:
   * "Para flaco, tampoco te pedí un testamento"
   
C) Dalto habla un 30% más rápido que el promedio de las personas:
   * ¿Cuánto tardaría el en decirlo?

"""

# Mi Solución

segundo = 1
palabras_por_segundo_promedio = 2

## Item A)

texto_usuario = input("Ingrese un texto: ")
cantidad_palabras_en_texto = len(texto_usuario.split())

calculo_tiempo = cantidad_palabras_en_texto * segundo / palabras_por_segundo_promedio

print("El tiempo promedio en decir el texto ingresado es de " + str(calculo_tiempo) + " segundos")
print("Hay " + str(cantidad_palabras_en_texto) + " palabras en el texto ingresado")

## Item B)

if (calculo_tiempo >= 60):
    print("Para flaco/a tampoco te pedí un testamento")

## Item C)
    
palabras_por_segundo_Dalto = 130 * 2 / 100 #Regla de 3 simple
calculo_tiempo_Dalto = cantidad_palabras_en_texto * segundo / palabras_por_segundo_Dalto

print("El tiempo promedio de Dalto en decir el texto ingresado es de " + str(round(calculo_tiempo_Dalto, 2)) + " segundos")



# Solución de Dalto:


frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(palabras_separadas)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diría en {cantidad_de_palabras / 2 * 0.7} segundos')











