import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import root_mean_squared_error

url = "https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador"
tablas = pd.read_html(url)

df_jugadores = tablas[0]
df_stats = tablas[1]

mlb_data = pd.concat([df_jugadores, df_stats], axis=1)

print(mlb_data.head())

faltantes = mlb_data.isnull().sum()
print(faltantes)

x = mlb_data["AB"]
y = mlb_data["R"]

corr, _ = pearsonr(x, y)
print(f"Pearson Correlation: {corr:.3f}")

plt.scatter(x, y, alpha=0.5, color="purple")
plt.title("Dispersion plot")
plt.xlabel("X - All Bats")
plt.ylabel("Y - Runs")
plt.grid(True)
plt.show()

x2 = mlb_data["AB"]
y2 = mlb_data["H"]

corr, _ = pearsonr(x2, y2)
print(f"Pearson Correlation: {corr:.3f}")

plt.scatter(x2, y2, alpha=0.5, color="purple")
plt.title("Dispersion plot")
plt.xlabel("X - All Bats")
plt.ylabel("Y - Hits")
plt.grid(True)
plt.show()

X = mlb_data[["AB"]]
y = mlb_data["H"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)

rmse = root_mean_squared_error(y_true=y_test, y_pred=predicciones)

print(f"El error (rmse) de test es: {rmse:.3f}")
