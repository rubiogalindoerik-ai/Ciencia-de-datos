# Semana 5 - Ciencia de datos

---

## Ventas de vehiculos y Sobrevivencia del Titanic

---

### Descripcion

Dividida en dos partes, la actividad te guiará a través del proceso de aplicación de técnicas avanzadas de ciencia de datos para resolver problemas reales, enfocándose en dos estudios de caso: predicción de ventas según el precio y el kilometraje de los vehículos y análisis de factores de sobrevivencia en el Titanic.

---

### Obejtivo

Reforzar los conocimientos sobre regresión lineal múltiple y regresión logística binaria para analizar datos y generar predicciones útiles en contextos de toma de decisiones.

---

### Instrucciones

#### Parte 1: Predicción de ventas usando regresión lineal múltiple

En esta sección de la actividad, crearás y evaluarás un modelo de regresión lineal múltiple para predecir las ventas de los vehículos de acuerdo con el precio de venta establecido y el kilometraje de los mismos.

1.**Preparación de los datos:** Guarda la base de datos en una variable. Los datos los obtendrás de la siguiente liga: <https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/download?datasetVersionNumber=1>

##### Librerias usadas

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
```

2.**Análisis exploratorio:** Realiza una gráfica de dispersión para verificar la relación que existe entre el precio, el kilometraje y las ventas. Para esto, utiliza pairplot de la biblioteca Seaborn, la cual te permitirá visualizar las relaciones entre estas variables.

```python
print("Información del dataset:")
print(df.head())
df.info()
df.describe()

sns.pairplot(df)
plt.show() # Grafica de dispersion entre todos los datos del dataset

columnas_interes = ["sellingprice", "mmr", "odometer"]

sns.set_theme(style="ticks")
pair_plot = sns.pairplot(df[columnas_interes], diag_kind="kde", plot_kws={"alpha": 0.6})

pair_plot.fig.suptitle(
    "Relación entre Precio de Venta, Precio Actual y Millas recorridas", y=1.02
)
plt.show() # Grafica de dispersion solo entre las variables del precio, el kilometraje y las ventas
```

3.**Identificación de variables:** Determina cuáles son las variables independientes y cuál es la dependiente: **Dependiente = Sellingprice, Independiente = odometer y mmr**

4.**División de datos:** Crea los grupos de entrenamiento y de prueba para tus variables. Esta división es esencial para entrenar tu modelo con un conjunto de datos y evaluar su rendimiento con otro, asegurando así que el modelo sea capaz de generalizar a nuevos datos.

```python
dfwnull = df.dropna(subset=["sellingprice", "mmr", "odometer"])

x = dfwnull[["mmr", "odometer"]]
y = dfwnull["sellingprice"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")
```

5.**Modelado:** Aplica el modelo de regresión lineal múltiple.

```python
modelo = LinearRegression()
```

6.**Evaluación del modelo:** Puedes utilizar métricas como el R² (coeficiente de determinación) para entender qué tan bien el modelo se ajusta a los datos.

```python
print(f"Coeficiente de determinación (R²): {r2_score(y_test, y_pred):.4f}")
print(f"Intersección (b): {modelo.intercept_}")
print(f"Coeficientes (m1, m2): {modelo.coef_}")
```

7.**Predicción:** Con el modelo ya entrenado y evaluado, procede a realizar las predicciones.

```python
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
```

8.**Error cuadrático medio:** Este paso te ayudará a entender la magnitud de los errores cometidos por el modelo en sus predicciones.

```python
mse = mean_squared_error(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"Raíz del Error Cuadrático Medio (RMSE): {mse**0.5:.2f}")
```

9.**Conclusión:** Finalmente, elabora una conclusión con base en los resultados obtenidos. Reflexiona sobre la eficacia del modelo de regresión lineal múltiple para predecir las ventas de vehículos. Considera posibles mejoras o ajustes para futuros modelos.

#### Conclusion

Con el coeficiente de determinación (R2) al 0.9686 se puede saber que las vaiables mmr y odometer son predictores fuertes para el precio de venta y con los coeficientes se ve que el precio del mercado y el precio de venta estan casi en una relacion 1 a 1 pues sube 0.98 mientras que el coeficiete de cada milla recorrida es el valor del auto disminuye

#### Reflexion

El modelo funciona bien pero mmr en ya es basicamente el precio, seria mejor predecir el precio sin este y usar otras variables para ver si estos aportan valor, que como se vio en la grafica que expulse en el punto 1, si puede ver que si afectan

---

#### Parte 2: Análisis de sobrevivencia en el Titanic con regresión logística binaria

Esta sección de la actividad se enfoca en la creación y evaluación de un modelo de regresión logística binaria. El objetivo principal será determinar las variables más significativas para predecir la sobrevivencia de los pasajeros del Titanic.

##### Librerias usadas

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from scipy import stats
```

1.**Preparación de los datos:** Guarda la base de datos en una variable. Los datos los obtendrás de la siguiente liga: <https://www.openml.org/data/get_csv/16826755/phpMYEkMl>.

```python
df = pd.read_csv("Datos/phpMYEkMl.csv")

print("Información del dataset:")
print(df.head())
```

2.**Limpieza de datos:** Examina las columnas disponibles en tu conjunto de datos y decide cuáles no son necesarias para tu análisis, elimina las que no consideres necesarias. Además, identifica los datos nulos que tengas y elimínalos.

```python
columnas_descarte = ["name", "ticket", "cabin", "boat", "body", "home.dest"]
df = df.drop(columns=columnas_descarte)
df = df.dropna()
df["sex"] = df["sex"].map({"male": 1, "female": 0})
df = pd.get_dummies(df, columns=["embarked"], drop_first=True)```

3.**Conversión de variables a su formato correcto:** Dependiendo de las variables en tu conjunto de datos, es posible que necesites convertir algunas de ellas a un tipo de dato más apropiado, como convertir variables categóricas a tipo 'category' o ajustar las fechas a un formato de fecha y hora.

```python
df = df.replace("?", np.nan)
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["fare"] = pd.to_numeric(df["fare"], errors="coerce")
df["age"] = df["age"].fillna(df["age"].median())
df["fare"] = df["fare"].fillna(df["fare"].median())
```

4.**Visualización de datos:** Analiza los datos de forma gráfica para verificar que existe una relación entre la variable dependiente y la independiente.

```python
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlación entre variables y Supervivencia")
plt.show()
```

![Imagen de la correlacion](Visualizaciones/Correlacion_variables_parte_2.png)

Como se puede ver en la imagen hay una fuerte correlacion entre las variables survived(Dependiente) y las demas que serian las independientes

5.**Prueba t-test:** Esta puede ayudarte a entender si las diferencias en las medias de dos grupos son estadísticamente significativas.

```python
sobrevivientes = df[df["survived"] == 1]["fare"]
no_sobrevivientes = df[df["survived"] == 0]["fare"]
t_stat, p_valor = stats.ttest_ind(sobrevivientes, no_sobrevivientes)
print("Resultados de la Prueba t-test (Variable: Tarifa/Fare)")
print(f"Media de tarifa (Sobrevivientes): {sobrevivientes.mean():.2f}")
print(f"Media de tarifa (No Sobrevivientes): {no_sobrevivientes.mean():.2f}")
print(f"Estadístico t: {t_stat:.4f}")
print(f"Valor p (p-value): {p_valor:.4e}")
alpha = 0.05
if p_valor < alpha:
    print("Existe una diferencia entre quienes sobrevivieron y quienes no.")
else:
    print("\nNo hay diferencia")
```

6.**División de datos:** Divide los datos en variables de prueba y de entrenamiento. Esto es crucial para entrenar el modelo y luego evaluar su capacidad para generalizar a nuevos datos.

```python
X = df.drop("survived", axis=1)
y = df["survived"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

7.**Creación del modelo:** Utiliza las clases vistas en la explicación de los temas para que puedas crear tu modelo.

```python
modelo_log = LogisticRegression(max_iter=1000)
modelo_log.fit(X_train, y_train)
```

8.**Estimación de los coeficientes y los odds ratio:** Una vez que entrenaste el modelo, el siguiente paso es interpretar los resultados. Esto se hace mediante la estimación de los coeficientes, los cuales te indicarán la fuerza y dirección de la relación entre cada variable independiente y la variable dependiente.

```python
y_pred = modelo_log.predict(X_test)
print(f"Precisión del modelo (Accuracy): {accuracy_score(y_test, y_pred):.4f}")
print("\nMatriz de Confusión:")
print(confusion_matrix(y_test, y_pred))
```

9.**Conclusión de tus resultados:** Formula una conclusión sobre tus hallazgos. Considera cuáles variables tienen mayor impacto en la probabilidad de sobrevivencia en el Titanic y la efectividad general de tu modelo para predecir la sobrevivencia. Reflexiona sobre posibles mejoras o ajustes para el modelo.

#### Conclusión

Con el t-test se ve claramente el favoritismo ecnomico que habia al momento de ver quienes sobrevivieron pues las medias de las tarfias de estos fue de 49.24 y de los que no sobrevivieron fue de 23.34 por lo que el dinero era un factor decisicivo al momento de acceder a los botes salvavidas, la precision del modelo es de 77.10% y se puede ver con la matriz de confusion que es bueno identificando a quienes sobreviviron aunque no es tan efectivo en los sobrevivientes

#### Reflexion

Mejorar el modelo no es facil pues los datos son viejos y la mayoria no son certeros, se puede ver por la cantidad de nulos que hay en areas como la edad, con esos datos podriamos mejorar la precision, tambien las creencias de esa epoca afectan a la prediccion, el hecho de que salvar a mujeres y niños diminuyera la posibilidad de salvarse siendo hombre no signidicaba que no te salvaras, sino que si eras de mayor clase social habian mas probabilidades de salvarte siendo hombre, por lo que la manera de mejorar el modelo y encontrando muchos de los datos faltantes y encontrar las distintas clases sociales que habian en el barco
