"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no
vegetarianas a sus clientes. Los ingredientes para cada tipo de
pizza aparecen a continuación.

*   Ingredientes vegetarianos: Pimiento y tofu.
*   Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza
vegetariana o no, y en función de su respuesta le muestre un
menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella
y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.
"""

# Mi solución:

print("Bienvenido/a a la pizzería Bella Napoli!!")
tipo_de_pizza = input("Quiere una pizza vegetariana? (S/N): ")

print("Recuerde que la Muzzarella y el tomate están en todas las pizzas")

ingredientes_vegetarianos_lista = ["pimiento", "tofu"]
ingredientes_vegetarianos_string = "pimiento tofu"
ingredientes_no_vegetarianos_lista = ["peperoni", "jamón", "salmón"]
ingredientes_no_vegetarianos_string = "peperoni jamón salmón jamon salmon"
ingredientes_obligatorios = " muzzarella y tomate"

if ((tipo_de_pizza == "S") or (tipo_de_pizza == "s")):
    print("Usted eligió: Tipo de Pizza Vegetariana")
    print("Elija un condimento extra para su pizza:")
    for condimento1 in ingredientes_vegetarianos_lista:
        print(condimento1)
    nuevo_ingrediente_vegetariano_input = input("Qué ingrediente vegetariano quiere?: ")
    if (ingredientes_vegetarianos_string.find(nuevo_ingrediente_vegetariano_input) != -1):
        ingrediente_extra = nuevo_ingrediente_vegetariano_input
    else:
        ingrediente_extra = ""
    print("Su pizza vegetariana tiene: " + ingrediente_extra + ingredientes_obligatorios)
else:
    print("Usted eligió: Tipo de Pizza NO Vegetariana")
    print("Elija un condimento extra para su pizza:")
    for condimento2 in ingredientes_no_vegetarianos_lista:
        print(condimento2)
    nuevo_ingrediente_no_vegetariano_input = input("Qué ingrediente vegetariano quiere?: ")
    if (ingredientes_no_vegetarianos_string.find(nuevo_ingrediente_no_vegetariano_input) != -1):
        ingrediente_extra = nuevo_ingrediente_no_vegetariano_input
    else:
        ingrediente_extra = ""
    print("Su pizza no vegetariana tiene: " + ingrediente_extra + ingredientes_obligatorios)



# Solución de la guía:

"""
### Presentación del menú con los tipos de pizza
print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")
### Decisión sobre el tipo de pizza
if tipo == "1":
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", end="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")
else:
    print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetarina con mozarrella, tomate y ", end="")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("jamón")
    else:
        print("salmón")
"""

