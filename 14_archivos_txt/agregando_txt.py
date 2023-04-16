cantidad_lineas = int(input("Ingrese la cantidad de líneas a escribir: "))
while (cantidad_lineas <= 0):
    cantidad_lineas = int(input("Reingrese una cantidad válida: "))

with open("./nuevo_txt.txt", "a", encoding="UTF-8") as archivo:
    # Agregando el archivo
    for i in range(cantidad_lineas):
        archivo.write(f"Línea {i+1} agregada\n")
    
    
# Usamos el permiso 'append'
