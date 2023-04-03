nombreProfesor = "Lucas Dalto"
nombreAlumno = input("Ingrese su nombre: ")

bienvenida = "Hola " + nombreAlumno + " bienvenido/a al curso de " + nombreProfesor
print(bienvenida)

'Otra forma de concatenar ==> los f strings'

bienvenida = f"Hola {nombreAlumno} bienvenido/a al curso de {nombreProfesor}"
print(bienvenida)
'Esto incluso sirve para concatenar strings con números'
a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = a + b
res_1 = f"El resultado de la suma de {a} + {b} es: {c}"
print(res_1)
'Podemos ver que todo lo convierte a texto sea un tipo de dato booleano, lista, diccionario, ... , ==> TODO'

