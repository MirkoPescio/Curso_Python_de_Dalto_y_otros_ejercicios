"""
Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente
será su NIF, y el valor será otro diccionario con los datos del cliente
(nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el
valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú:
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente,
(4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:

* Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a
    la base de datos.
* Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
* Preguntar por el NIF del cliente y mostrar sus datos.
* Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
* Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
* Terminar el programa.

"""

# Mi solución:

dicc_clientes = {}
print("Entrando a la base de datos de clientes de la empresa Best Buy Argentina")
print("Opciones: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar")
opcion = int(input("Elija alguna de las opciones (1, 2, 3, 4, 5, 6): "))

while((opcion <= 0)):
    opcion = input("Reingrese una opción válida: ")
    
### Opción 1: Añadir cliente
while (opcion == 1):
    print("Usted eligió la opción 1: Añadir Cliente")
    NIF = int(input("Ingrese el NIF del cliente: "))
    nombre = input("Nombre del cliente: ")
    direccion = input("Dirección del cliente: ")
    telefono = input("Teléfono del cliente: ")
    correo = input("Correo electrónico: ")
    preferente = input("El cliente es preferente? (True/False): ")
    dicc_clientes[NIF] = {'nombre': nombre, 'dirección': direccion, 'teléfono': telefono, 'correo': correo, 'preferente': preferente}
    opcion = int(input('¿Con cuál opción quiere seguir?: '))

### Opción 2: Eliminar cliente
    
while (opcion == 2):
    print("Usted eligió la opción 2: Eliminar Cliente")
    eliminar_NIF = int(input("Ingrese el NIF del cliente que va a eliminar: "))
    dicc_clientes.pop(eliminar_NIF)
    opcion = int(input('¿Con cuál opción quiere seguir?: '))

### Opción 3: Mostrar cliente

while (opcion == 3):
    print("Usted eligió la opción 3: Mostrar Cliente")
    mostrar_NIF = int(input("Ingrese el NIF del cliente que quiere ver: "))
    for NIF, datos in dicc_clientes.items():
        if (mostrar_NIF == NIF):
            print(NIF, datos)
    opcion = int(input('¿Con cuál opción quiere seguir?: '))

### Opción 4: Listar todos los clientes

while (opcion == 4):
    print("Usted eligió la opción 4: Listar Todos los Clientes")
    lista_todos = []
    for NIF, datos in dicc_clientes.items():
        lista_todos.append((NIF, datos))
    print(lista_todos)
    opcion = int(input('¿Con cuál opción quiere seguir?: '))
    
### Opción 5: Listar clientes preferentes
    
while (opcion == 5):
    print("Usted eligió la opción 5: Listar Clientes Preferentes")
    lista_preferentes = []
    for NIF, datos in dicc_clientes.items():
        if(datos['preferente'] == 'True'):
            lista_preferentes.append((NIF, datos))
    print(lista_preferentes)
    opcion = int(input('¿Con cuál opción quiere seguir?: '))
    
### Opción 6: Terminar
    
while (opcion == 6):
    print("Usted eligió la opción 6: Terminando proceso...")
    break


# Solución de la guía:

"""
clientes = {}
opcion = ''
while opcion != '6':
    if opcion == '1':
        nif = input('Introduce NIF del cliente: ')
        nombre = input('Introduce el nombre del cliente: ')
        direccion = input('Introduce la dirección del cliente: ')
        telefono = input('Introduce el teléfono del cliente: ')
        email = input('Introduce el correo electrónico del cliente: ')
        vip = input('¿Es un cliente preferente (S/N)? ')
        cliente = {'nombre':nombre, 'dirección':direccion, 'teléfono':telefono, 'email':email, 'preferente':vip=='S'}
        clientes[nif] = cliente
    if opcion == '2':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            del clientes[nif]
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '3':
        nif = input('Introduce NIF del cliente: ')
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print('No existe el cliente con el nif', nif)
    if opcion == '4':
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if opcion == '5':
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    opcion = input('Menú de opciones\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar clientes\n(5) Listar clientes preferentes\n(6) Terminar\nElige una opción:')
"""

