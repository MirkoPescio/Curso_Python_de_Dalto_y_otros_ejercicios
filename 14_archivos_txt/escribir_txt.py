
with open("./texto_de_Mirko.txt", "w", encoding="UTF-8") as archivo:
    # Sobre-escribiendo el archivo
    # archivo.write("1era sobre-escritura del archivo TXT")
    archivo.writelines(["Hola, buenos días/tardes/noches\n"])
    archivo.writelines(["¿Cómo te va en el curso de Python?", " Espero que bien"])
    


