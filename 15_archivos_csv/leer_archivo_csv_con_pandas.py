import pandas as pd

print(type(pd))

# Usando la función read_csv para leer el archivo CSV


df = pd.read_csv("./datos.csv")
print(df)

print("\n")

# df significa dataframe

nombres = df["nombre"]
print(nombres)

print("\n")

"""
# También puedo llamar a los datos con los parámetros que yo quiera:
    
df = pd.read_csv("./datos.csv", names=["name", "lastname", "age"])

nombres = df["name"]
print(nombres)
"""

# Ordenamos los datos por la edad de menor a mayor

df_ordenado = df.sort_values("edad")
print(df_ordenado)

print("\n")

# Ordenamos los datos por la edad de mayor a menor

df_ordenado_invertido = df.sort_values("edad", ascending=False)
print(df_ordenado_invertido)

print("\n")

# Método para concatenar dataframes

df1 = pd.read_csv("./datos.csv")
df2 = pd.read_csv("./datos.csv")

df_concatenado = pd.concat([df1, df2])
print(df_concatenado)

print("\n")

# Accediendo a las primeras filas por cantidad con el método head()

primer_fila = df.head(1)
ver_2_primeras_filas = df.head(2)
ver_3_primeras_filas = df.head(3)

print(primer_fila)
print("\n")

print(ver_2_primeras_filas)
print("\n")

print(ver_3_primeras_filas)
print("\n")

# Accediendo a las últimas filas por cantidad con el método tail()

ultima_fila = df.tail(1)
ultimas_2_filas = df.tail(2)

print(ultima_fila)
print("\n")

print(ultimas_2_filas)
print("\n")

# Accediendo a la cantidad de filas y columnas con shape

filas_totales, columnas_totales = df.shape

print(f'Cantidad total de filas: {filas_totales}')
print(f'Cantidad total de columnas: {columnas_totales}')
print("\n")

# Obteniendo data estadística del data frame:
    
data_info = df.describe()

print(data_info) # Esto es usado en ciencias de datos e inteligencia artificial
print("\n")

# Accediendo a un elemento específico del dataframe con loc

elemento_especifico_loc_1 = df.loc[2, "edad"]
elemento_especifico_loc_2 = df.loc[3, "apellido"]

print(elemento_especifico_loc_1)
print(elemento_especifico_loc_2)
print("\n")

# Accediendo a un elemento específico del dataframe con iloc
## A diferencia de loc, con iloc accedemos únicamente por los índices

elemento_especifico_iloc_1 = df.iloc[0, 1]
elemento_especifico_iloc_2 = df.iloc[3, 0]

print(elemento_especifico_iloc_1)
print(elemento_especifico_iloc_2)
print("\n")

todos_los_nombres = df.iloc[:, 0]
todos_los_apellidos = df.iloc[:, 1]

print(todos_los_nombres)
print("\n")
print(todos_los_apellidos)
print("\n")

# Accediendo a la fila 3 con loc (para mostrar todos los datos de la fila)

datos_fila_3 = df.loc[2, :]

print(datos_fila_3)
print("\n")

# Accediendo a filas cuyo dato edad sea mayor a 30:
    
mayor_que_30 = df.loc[df["edad"]>30, :]

print("Mostrando filas cuyo dato edad sea mayor que 30")
print(mayor_que_30)
print("\n")

menor_que_30 = df.loc[df["edad"]<30, :]

print("Mostrando filas cuyo dato edad sea menor que 30")
print(menor_que_30)
print("\n")

