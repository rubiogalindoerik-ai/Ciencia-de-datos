# Proyecto: Entrega final - Ciencia de datos

---

## Mercado inmobiliario

---

### Descripción

En la segunda fase del proyecto, aplicarás técnicas avanzadas de ciencia de datos
para desarrollar modelos predictivos basados en los datos explorados anteriormente.
Asimismo, utilizarás técnicas de visualización de datos avanzadas para comunicar de
forma eficiente los insights obtenidos.

---

### Objetivo

Aplicar técnicas de modelado predictivo para analizar el mercado inmobiliario y
comunicar los resultados de manera efectiva.

---

### Requerimientos

- Los datos obtenidos en la fase I (Avance del Proyecto).
- Google Colab o entorno local con Python.

---

### Instrucciones

#### Parte 1: Modelo de regresión lineal múltiple

1.**Limpieza de datos:** utiliza Pandas para limpiar tus datos. Incluye la
eliminación o imputación de valores faltantes e identificación y corrección de
errores (por ejemplo: valores atípicos extremos que claramente son incorrectos).

```python
import pandas as pd

df = pd.read_csv("Datos/train2.csv")

# Llenamos con la mediana
columnas_a_imputar = ["bedrooms", "bathrooms", "beds"]
for col in columnas_a_imputar:
    df[col] = df[col].fillna(df[col].median())

# Borramos la fila si falta el precio
df = df.dropna(subset=["log_price"])

# Dejamos solo lo importante
columnas_relevantes = [
    "log_price",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "beds",
    "number_of_reviews",
    "review_scores_rating",
]
df_limpio = df[columnas_relevantes].copy()

# Se crea el archivo con todo lo hecho antes
df_limpio.to_csv("Datos/train2_limpio.csv", index=False)

print(f"Limpieza exitosa. Filas originales: {len(df)}, Filas finales: {len(df_limpio)}")
print("Nuevo archivo guardado")
```

2.**Identificación de variables:** define cuál es la variable dependiente y cuáles
son las variables independientes.

La varible dependiente es el precio mientras que el resto son independientes

3.**Selección de características:** determina qué variables incluir en el modelo.
Esto puede requerir realizar más análisis exploratorio para evaluar la importancia
de las distintas características.

```python
y = df['log_price']
X = df[['accommodates', 'bedrooms', 'bathrooms', 'review_scores_rating']]
```

4.**Análisis de correlación:** emplea Seaborn para generar un pairplot que muestre
las relaciones entre las variables.

```python
sns.set_theme(style="ticks")
grafica = sns.pairplot(df, diag_kind="kde", plot_kws={"alpha": 0.5})
grafica.fig.suptitle("Relaciones entre Variables de Vivienda y Precio", y=1.02)
plt.show()
```

5.**Grupos de entrenamiento y prueba:** divide el conjunto de datos en un grupo de
entrenamiento y otro de prueba.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")
```

6.**Construcción y entrenamiento del modelo:** construye y entrena un modelo de
regresión lineal múltiple con las variables seleccionadas. Es importante considerar
la multicolinealidad y la relevancia de cada variable en el modelo.

```python
modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
print(f"Intersección (b): {modelo.intercept_:.4f}")
for nombre, coef in zip(X.columns, modelo.coef_):
    print(f"{nombre}: {coef:.4f}")
```

7.**Evaluación del modelo:** evalúa el modelo mediante métricas de regresión,
enfocándote en el R² y el ajuste de los datos. Interpreta estos valores para
entender la calidad del modelo.

```python
print(f"Coeficiente de determinación (R²): {r2_score(y_test, y_pred):.4f}")
```

Coeficiente de determinación (R²): 0.3691, por lo que el modelo solo muestra
el 36% de la variabilidad del precio el resto depende de otros factores como
su ubicacion o cosas de ese tipo

8.**Predicciones:** utiliza el modelo para realizar predicciones sobre el conjunto
de prueba y comparar estas predicciones con los valores reales para evaluar la
precisión del modelo.

```python
comparacion = pd.DataFrame({"Valor Real": y_test, "Predicción": y_pred})
print("\nCOMPARACION DE VALORES")
print(comparacion.head(10))
```

9.**Cálculo del error cuadrático medio (MSE):** calcula el MSE como una medida del
error de las predicciones realizadas por el modelo.

```python
print(f"Error Cuadrático Medio (MSE): {mse:.4f}")
```

#### Parte 2: Comunicación de los resultados

1.Crea visualizaciones que comuniquen los resultados del modelo, como gráficos de
dispersión de predicciones vs. valores reales o gráficos de importancia de las
características.

```python
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
```

2.Desarrolla una narrativa que acompañe a las visualizaciones, y explica los
resultados del análisis, la precisión del modelo y cómo las características
influyen en los precios de las viviendas.

![Imagen con las correlaciones entre las variables](Proyectp/Final/Visualizaciones/pairplot_correlacion.png)

En estas multiples graficas podemos ver como el precio aumenta principalmente
en la cantidad de cuartos o comodidades demostrando que entre mas espacio mayor
el precio ademas que tanto la cantidad de reviws y el puntaje de las reviews no
afectan al significativamente al precio

![Grafica de la comparacion entre los valores reales y predicciones](Proyecto/Final/Visualizaciones/comparacion_final.png)

En esta grafica se puede ver que el modelo es bueno prediciendo los que son de precio
medio esto se ve por como conde los puntos estan concentrados tambien es donde se encuentra
la linea roja pero conforme sube el precio las predicciones se dispersan lo que muestra que
como se dijo antes con el coeficiente de correlacion hay mas factores que afectan al
precio final del alojamiento tambien se colabora con el error cuadratico medio que es
relativamente bajo por lo que los valores dispersos no estan lejos de los valores reales
