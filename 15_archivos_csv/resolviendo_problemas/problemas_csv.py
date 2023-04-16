import pandas as pd


df = pd.read_csv("./heroes.csv")

# Cambiar el tipo de dato de una columna

# Convertimos a string los datos de una columna
df["ranking"] = df["ranking"].astype(str)
print(df["ranking"])
print("\n")

# Mostramos el tipo de dato del primer elemento de la columna edad
print(type(df["ranking"][0]))
print("\n")

# Reeplazando valores
df["grupo"].replace("Avengers", "Vengadores", inplace=True)
df["grupo"].replace("Justice League", "Liga de la Justicia", inplace=True)
print(df["grupo"])
print("\n")

# Eliminando filas con datos vacíos:

df = df.dropna()
print(df)
print("\n")

df = df.drop_duplicates()
print(df)
print("\n")

# Creando un CSV con el dataframe resultante (limpio)
df.to_csv("./datos_limpios.csv")
