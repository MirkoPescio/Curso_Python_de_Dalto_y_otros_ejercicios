import csv

with open("./datos.csv") as archivo:
    reader = csv.reader(archivo)
    print(reader)
    for row in reader:
        print(row)

    
    