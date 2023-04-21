class Book:
    # Método: una función asociada a un objeto
    def __init__(self, title, author, price, stock, oid):
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._oid = oid
        # Definimos nuestras clases como protegidas

    # Definimos una función para mostrar la información completa:
    def getinfo(self):
        return f"""\nTítulo => {self._title}\nAutor => {self._author}\nPrecio => ${self._price}\nStock disponible => {self._stock} unidades"""
    
    # Nomenclatura para las propiedades de los objetos:

    ## público -> accesible para todos
    ## protegido _ -> solo debería accederse desde la propia clase y sus subclases
    ## private __ -> solo es accesible por su propia clase

    # Getters / Setters

    ## get -> obtener (lectura)
    ## set -> setear/establecerModificarValores (escritura)

    def get_title(self):
        return self._title
    def set_title(self, new_title):
        self._title = new_title

    def get_price(self):
        return self._price
    def set_price(self, new_price):
        if (new_price > 0):
            self._price = new_price
        else:
            print("El precio de un libro no puede ser igual a 0 o menor")

# La clase de Comics hereda propiedades de la clase super: Book

class Comic(Book):
    def __init__(self, title, author, price, stock, oid, ilustrators, vol):
        super().__init__(title, author, price, stock, oid)
        self._ilustrators = ilustrators
        self._vol = vol
    
    def getinfo(self):
        info = super().getinfo()
        str_ilustrators = ', '.join(self._ilustrators) # Pasamos a string, los ilustradores de la lista
        return info + f"""\nIlustradores => {str_ilustrators}\nVolumen => {self._vol}"""


# Instanciar

book_1 = Book('El Quijote', 'Miguel de Cervantes', 750.00, 24, 1)

print(book_1) # Me devuelve que es de Tipo Object

# Para acceder a las propiedades del objeto:
print(book_1._title) 
print(book_1._stock)
print("\n")

book_2 = Book('1984', 'G. Orwell', 150.00, 50, 2)
print(book_2._title)
print(book_2._author)
print("\n")

# Imprimiendo toda la información de los libros:
print(book_1.getinfo())
print("\n")
print(book_2.getinfo())
print("\n")

# Usando método GET:
print(book_1.get_title())
print("\n")

# Usando método SET:
book_2.set_title('Hola Mundo!!')
print(book_2.get_title())
print("\n")

# Mostrando una excepción:
book_1.set_price(0)
print("\n")



# Pasando a la clase Comic

comic_1 = Comic("Batman: The Killing Joke", "Alan Moore", 1600.20, 12, 1, ["Ilust1", "Ilust2"], "#1")
print(comic_1)
print(comic_1.get_title())
print("\n")

print(comic_1.getinfo())
print("\n")
