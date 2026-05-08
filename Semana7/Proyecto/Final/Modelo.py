import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df = pd.read_csv("Datos/train2_limpio.csv")

y = df["log_price"]
X = df[["accommodates", "bedrooms", "bathrooms", "review_scores_rating"]]

sns.set_theme(style="ticks")
grafica = sns.pairplot(df, diag_kind="kde", plot_kws={"alpha": 0.5})
grafica.fig.suptitle("Relaciones entre Variables de Vivienda y Precio", y=1.02)
plt.show()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")

modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Intersección (b): {modelo.intercept_:.4f}")
for nombre, coef in zip(X.columns, modelo.coef_):
    print(f"{nombre}: {coef:.4f}")

print(f"Coeficiente de determinación (R²): {r2_score(y_test, y_pred):.4f}")

comparacion = pd.DataFrame({"Valor Real": y_test, "Predicción": y_pred})
print("\nCOMPARACION DE VALORES")
print(comparacion.head(10))

print(f"Error Cuadrático Medio (MSE): {mse:.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, color="blue", alpha=0.4, label="Predicciones")
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    color="red",
    lw=2,
    label="Ajuste Ideal",
)
plt.title("Comparación de Valores Reales vs Predicciones")
plt.xlabel("Valores Reales (log_price)")
plt.ylabel("Predicciones (log_price)")
plt.legend()
plt.grid(True)
plt.show()

X_train_with_const = sm.add_constant(X_train)
modelo_stats = sm.OLS(y_train, X_train_with_const).fit()
print("P-VALUE", modelo_stats.summary())
