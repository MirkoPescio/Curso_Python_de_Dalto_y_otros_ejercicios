import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("./16_archivos_problemas_graficos/dispersion.csv")

# Creando el gráfico
sns.scatterplot(x="tiempo", y="dinero", data=df)

# Mostrando el gráfico
plt.show()
