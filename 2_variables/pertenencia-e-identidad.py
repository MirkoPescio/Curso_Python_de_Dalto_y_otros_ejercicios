nombre = input("Ingrese su nombre: ")

# Concatenar con f-strings
bienvenida = f"Hola {nombre}. Te damos la bienvenida al curso de Lucas Dalto"
print(bienvenida)

# Concatenar con +
bienvenida2 = "Hola " + nombre + ". Te damos la bienvenida al curso de Lucas Dalto"
print(bienvenida2)


'operadores de pertenencia en strings: (in / not in)'

print("ola" in bienvenida); 'Me tendría que responder True'
print(nombre in bienvenida); 'Me tendría que responder True'
print("Pedro" in bienvenida); 'Me tendría que responder False'
print("Dalto" not in bienvenida); 'Me tendría que responder False ya que "Dalto" sí está en el String Bienvenida'
print("hola" in bienvenida); 'Me responde False ya que "Hola" es distinto que "hola"'
