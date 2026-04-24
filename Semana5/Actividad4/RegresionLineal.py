import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("Datos/car_prices.csv")

print("Información del dataset:")
print(df.head())
df.info()
df.describe()

sns.pairplot(df)
plt.show()

columnas_interes = ["sellingprice", "mmr", "odometer"]

sns.set_theme(style="ticks")
pair_plot = sns.pairplot(df[columnas_interes], diag_kind="kde", plot_kws={"alpha": 0.6})

pair_plot.fig.suptitle(
    "Relación entre Precio de Venta, Precio Actual y Millas recorridas", y=1.02
)
plt.show()

dfwnull = df.dropna(subset=["sellingprice", "mmr", "odometer"])

x = dfwnull[["mmr", "odometer"]]
y = dfwnull["sellingprice"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")

modelo = LinearRegression()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

print(f"Coeficiente de determinación (R²): {r2_score(y_test, y_pred):.4f}")
print(f"Intersección (b): {modelo.intercept_}")
print(f"Coeficientes (m1, m2): {modelo.coef_}")
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Raíz del Error Cuadrático Medio (RMSE): {mse**0.5:.2f}")
