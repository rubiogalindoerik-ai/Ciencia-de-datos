import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("train2.csv")

# Analisis
print("Información del dataset:")
df.info()
df.describe()
print("Mediana:\n", df.median(numeric_only=True))
print("\nDesviación estándar:\n", df.std(numeric_only=True))

# Histrograma
plt.figure()
plt.hist(df["price"], bins=50)
plt.title("Distribución de precios")
plt.xlabel("Precio")
plt.ylabel("Frecuencia")
plt.savefig("hist_precio.png")
plt.show()

# Boxplot
plt.figure()
sns.boxplot(x=df["price"])
plt.title("Boxplot del precio")
plt.savefig("boxplot_precio.png")
plt.show()

# Grafico de barras
plt.figure()
df["room_type"].value_counts().plot(kind="bar")
plt.title("Tipo de habitación")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.savefig("barras_room_type.png")
plt.show()

# Scatter
plt.figure()
plt.scatter(df["availability_365"], df["price"])
plt.xlabel("Disponibilidad")
plt.ylabel("Precio")
plt.title("Precio vs Disponibilidad")
plt.savefig("scatter_precio_disponibilidad.png")
plt.show()

# Mapa de calor
plt.figure()
corr = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr, annot=True)
plt.title("Correlación entre variables")
plt.savefig("heatmap.png")
plt.show()
