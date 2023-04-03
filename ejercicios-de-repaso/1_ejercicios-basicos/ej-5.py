"""
Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora.
Después debe mostrar por pantalla la paga que le corresponde.
"""

# Mi solución

paga_por_hora = int(input("Ingrese el valor de paga por hora: "))
nombre_empleado = input("Ingrese el nombre del empleado/a: ")
horas_trabajadas = int(input("Ingrese la cantidad de horas que trabajó: "))
pago_total = paga_por_hora * horas_trabajadas
print("El/la empleado/a " + nombre_empleado + " hoy trabajó " + str(horas_trabajadas) + " por lo tanto su paga es de: $" + str(pago_total))

# Solución de la página web:

"""
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
paga = horas * coste
print("Tu paga es", paga)
"""