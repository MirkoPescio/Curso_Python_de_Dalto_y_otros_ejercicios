ingreso_mensual = int(input("Ingrese su haber mensual: "))
gasto_mensual = int(input("Ingrese su gasto mensual: "))

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit. Ya que su monto en contra es de: $" + str(ingreso_mensual - gasto_mensual))
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Estás bien en cualquier parte del mundo")
    else:
        print("Estás gastando mucho! Hay que ver si te alcanza en cualquier parte del mundo")
elif ingreso_mensual > 1000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit. Ya que su monto en contra es de: $" + str(ingreso_mensual - gasto_mensual))
    elif ingreso_mensual - gasto_mensual > 580:
        print("Estás bien en latinoamérica")
    else:
        print("Estás gastando mucho! Hay que ver si te alcanza en todo latinoamérica")
elif ingreso_mensual > 500:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit. Ya que su monto en contra es de: $" + str(ingreso_mensual - gasto_mensual))
    elif ingreso_mensual - gasto_mensual > 200:
        print("Estás bien en Argentina")
    else:
        print("Estás gastando mucho! Hay que ver si te alcanza en Argentina")
elif ingreso_mensual > 200:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit. Ya que su monto en contra es de: $" + str(ingreso_mensual - gasto_mensual))
    elif ingreso_mensual - gasto_mensual > 80:
        print("Estás bien en Venezuela")
    else:
        print("Estás gastando mucho! Hay que ver si te alcanza")
else:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en déficit. Ya que su monto en contra es de: $" + str(ingreso_mensual - gasto_mensual))
        print("Y también sos pobre")
    else:
        print("Sos pobre")

