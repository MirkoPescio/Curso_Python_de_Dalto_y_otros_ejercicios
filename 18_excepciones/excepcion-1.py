def sumar_dos_n():
    while(True):
        num1 = input("Ingrese el primer número: ")
        num2 = input("Ingrese el segundo número: ")
        try:
            resultado = int(num1) + int(num2)
        except:
            print("Te pedí un número salame, no te hagas el gracioso")
        else:
            break
        finally:
            print("Esto se ejecuta siempre")
    return resultado

def main():
    suma = sumar_dos_n()
    print(suma)
main()
