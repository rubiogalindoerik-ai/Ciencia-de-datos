import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

x = np.linspace(0, 10, 100)
y = np.sin(x)
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 2 - 1
data_hist = np.random.randn(1000)
categories = ["A", "B", "C", "D"]
values = [23, 45, 12, 30]

# Crear visualizaciones:
# 1. Gráfico de línea básico
# 2. Gráfico de dispersión
# 3. Histograma
# 4. Gráfico de barras
# 5. Personalizar: títulos, etiquetas, leyenda, colores

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="Seno(x)", color="blue", linestyle="-", linewidth=2)
plt.title("Gráfico de Línea - Función Seno")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(
    x_scatter,
    y_scatter,
    label="Datos Aleatorios",
    color="purple",
    marker="o",
    s=50,
    alpha=0.6,
)
plt.title("Gráfico de Dispersión")
plt.xlabel("Valores X")
plt.ylabel("Valores Y")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.hist(
    data_hist, bins=30, label="Frecuencia", color="green", edgecolor="black", alpha=0.7
)
plt.title("Histograma de Datos")
plt.xlabel("Valores")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.bar(
    categories,
    values,
    label="Ventas por Categoría",
    color=["coral", "teal", "gold", "orchid"],
    edgecolor="navy",
)
plt.title("Gráfico de Barras")
plt.xlabel("Categorías")
plt.ylabel("Valores")
plt.legend()
plt.grid(axis="y")
plt.show()

# Usando un dataset (puede ser 'iris' o cualquier otro)

# Ejercicios:
# 1. Cargar dataset y mostrar info básica
# 2. Calcular estadísticas descriptivas
# 3. Crear histogramas de todas las columnas numéricas
# 4. Crear matriz de correlación
# 5. Crear boxplots por categoría
# 6. Identificar outliers

df = sns.load_dataset("iris")

print("--- Información Básica ---")
print(df.info())
print("\n--- Primeras 5 filas ---")
print(df.head())

print("\n--- Estadísticas Descriptivas ---")
print(df.describe())

df.select_dtypes(include=["number"]).hist(
    figsize=(10, 8), color="skyblue", edgecolor="black"
)
plt.suptitle("Distribución de Variables Numéricas", fontsize=16)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
corr_matrix = df.select_dtypes(include=["number"]).corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Matriz de Correlación")
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x="species", y="sepal_length", palette="Set2")
plt.title("Distribución de Sepal Length por Especie")
plt.show()


def identificar_outliers(columna):
    Q1 = columna.quantile(0.25)
    Q3 = columna.quantile(0.75)
    IQR = Q3 - Q1
    limite_inferior = Q1 - 1.5 * IQR
    limite_superior = Q3 + 1.5 * IQR
    return columna[(columna < limite_inferior) | (columna > limite_superior)]


print("\n--- Outliers Detectados ---")
for col in df.select_dtypes(include=["number"]).columns:
    outliers = identificar_outliers(df[col])
    if not outliers.empty:
        print(f"Columna '{col}' tiene {len(outliers)} outliers:\n{outliers.values}")
    else:
        print(f"Columna '{col}' no tiene outliers.")
