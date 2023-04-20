import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("./16_archivos_problemas_graficos/flexiones.csv")

# Creando el gráfico
sns.lineplot(x="fecha", y="cantidad-flexiones", data=df)

# Identificamos el punto más alto con un punto:
plt.plot("01-15", 45, "o")

# Mostrando el gráfico
plt.show()
