"""
Ejercicio 7
Escribir un programa que pregunte el correo electrónico del usuario en la consola 
y muestre por pantalla otro correo electrónico con el mismo nombre 
(la parte delante de la arroba @) pero con dominio ceu.es.
"""

# Mi solución:

correo_usuario = input("Ingrese su correo electrónico: ")

while not "@" in correo_usuario:
    correo_usuario = input("Ingrese un correo electrónico válido: ")

print("Correo electrónico actual: " + correo_usuario)
nuevo_dominio = "@ceu.es"

sin_dominio = correo_usuario.split("@")[0]
nuevo_correo = sin_dominio + nuevo_dominio
print("Tu nuevo correo es: " + nuevo_correo)


# Solución de la guía:

email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')
