'El operador "del" elimina variables declaradas'

a = 20
b = 15
c = 320
d = 500
del c
e = a + b + c + d
res_1 = f"El resultado de la suma e es: {e}"
print(res_1)

"Es normal que aparezca un error ya que eliminamos la variable c antes de ejecutar la operación e"