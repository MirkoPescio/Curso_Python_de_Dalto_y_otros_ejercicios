import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:/Users/Mirko/Desktop/curso_de_Dalto/16_archivos_problemas_graficos/cofla_ingresos.csv")

# Creando el gráfico
sns.barplot(x="fuentes", y="ingresos", data=df)

# Identificamos el punto más alto con un punto:
plt.plot("Trabajo Fijo", 3000, "o")

# Obteniendo el total de ingresos:
total_ingresos = df["ingresos"].sum()

# Mostrando el total:
print(f'El total de ingresos de Cofla es de ${total_ingresos} U$S')

# Mostrando el gráfico
plt.show()
