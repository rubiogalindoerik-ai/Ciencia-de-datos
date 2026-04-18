# Actividad 4 - Ciencia de datos

---

## Equipos de beisbol

---

### Descripcion

Esta actividad se centra en aplicar y profundizar los conocimientos y habilidades que adquiriste en los temas 9 al 12. A través de un conjunto de datos reales, relacionados con el rendimiento de equipos de béisbol, tendrás la oportunidad de practicar técnicas esenciales en el proceso de ciencia de datos, desde la adquisición y preparación de datos hasta la modelación, predicción y evaluación de resultados.

---

### Objetivo

Reforzar los conceptos de regresión lineal simple y limpieza de datos, utilizando datos reales de equipos de béisbol, para predecir el número de carreras (runs) basado en el número de bateos.

---

### Instrucciones

En esta actividad, crearás y evaluarás un modelo de regresión lineal simple con el objetivo de predecir el número de runs de los equipos de béisbol de acuerdo con el número de bateos que tienen.

#### Parte 1: Preparación de los datos

1. **Obtención de los datos:** Guarda la base de datos en una variable. Los datos los encontrarás en la siguiente página: <https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador>

2. **Limpieza y preparación de los datos:** Evalúa los datos recopilados en busca de valores faltantes o erróneos. Además, realiza la limpieza necesaria, la imputación de datos faltantes y la estandarización de los datos para asegurar su calidad y uniformidad.

#### Parte 2: Modelado y evaluación

Continúa con el desarrollo del modelo de regresión lineal simple. Para esto, realiza lo siguiente:

1.**Análisis exploratorio:** Calcula la correlación de Pearson para determinar la relación entre el número de bateos y carreras. Interpreta este coeficiente para entender la fuerza y dirección de la relación.

```python
import pandas as pd
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr

url = "https://www.espn.com.mx/beisbol/mlb/estadisticas/jugador"
tablas = pd.read_html(url)

df_jugadores = tablas[0]
df_stats = tablas[1]

mlb_data = pd.concat([df_jugadores, df_stats], axis=1)

print(mlb_data.head())

faltantes = mlb_data.isnull().sum()
print(faltantes)

x = mlb_data["H"]
y = mlb_data["R"]

corr, _ = pearsonr(x, y)
print(f"Pearson Correlation: {corr:.3f}")

plt.scatter(x, y, alpha=0.5, color="purple")
plt.title("Dispersion plot")
plt.xlabel("X - Hits")
plt.ylabel("Y - Runs")
plt.grid(True)
plt.show()
```

![Tabla de resultados nulos](img/resulnull.png)  
![Grafica de dispersion entre la carrera y los bateos](img/tdishr.png)  
En la imagen se puede ver que no hay datos vacios (nulos) por lo que no es necesario una limpieza en los datos y en la grafica de dispersion ademas de la correlación de pearson no se ve que las carreras y los bateos no tienen correlación, el coeficiente de pearson es de 0.413 lo cual no es suficiente para hacer un modelo

2.**Construcción del modelo:** Identifica tu variable dependiente y tu variable independiente. Divide el conjunto de datos en dos grupos: uno para entrenamiento y otro para prueba.

```python
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
```

![Grafica de dispersion entre todos los bateos y los hits](tdiabh.png)  
Identifique que la variable con mayor correlacion fue bateos totales y hits, obvio ya que a mayor cantidad de oportunidades mayor cantidad de exitos probables y la cantidad de dato de entrenamiento fue: 40 y de prueba: 10

```python
X = mlb_data[["AB"]]
y = mlb_data["H"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")
```

3.**Entrenamiento y predicción:** Entrena tu modelo de regresión lineal simple con el conjunto de entrenamiento. Luego, utiliza este modelo para realizar predicciones sobre el conjunto de prueba.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)
```

4.**Evaluación:** Calcula el error de tus predicciones utilizando métricas adecuadas. Analiza estos errores para evaluar la precisión de tu modelo.

```python
rmse = root_mean_squared_error(y_true=y_test, y_pred=predicciones)

print(f"El error (rmse) de test es: {rmse:.3f}")
```

5.**Conclusión:** Reflexiona sobre los resultados obtenidos, discute la efectividad del modelo y su aplicabilidad en la toma de decisiones estratégicas basadas en el análisis de datos.  
Ya con las variables de mayor correlacion, con la correlacion de pearson dando un 0.868 y calculando el error que da un 1.101 se puede ver que el modelo solo falla por un hit lo cual es bastante bajo y implica que el modelo de regresion lineal funciona bien con esta base de datos ahora es aplicable para la toma de decisiones como por ejemplo: la evaluacion de rendimiento, si un jugador esta por debajo del promedio respecto a la cantidad de oportunidades implicara que su najo rendimiento no tiene nada que ver con la mala suerte ni la falta de oportunidades, tambien se pueden hacer proyecciones, se puede ver cuantos hits aportara un jugador si se le dan cierta cantidad de oportunidades

---

## Ejercicios Complementarios

---

### Ejercicios de Normalización y Estandarización

#### Ejercicio 1: Normalización Min-Max

La fórmula de normalización Min-Max es:

```
X_normalized = (X - X_min) / (X_max - X_min)
```

Dados los datos: [10, 20, 30, 40, 50]

1. Aplicar Min-Max normalization manualmente
2. Verificar que el resultado esté entre 0 y 1
3. Implementar en Python

```python
datos = [10, 20, 30, 40, 50]

X_min = min(datos)
X_max = max(datos)

X_normalized = lambda X: (X - X_min) / (X_max - X_min)
resultado = [X_normalized(x) for x in datos]

print(f"Resultado de la normalizacion: {resultado}")

```

#### Ejercicio 2: Estandarización (Z-Score)

La fórmula de estandarización es:

```
Z = (X - μ) / σ
```

Donde μ = media y σ = desviación estándar

Dados los datos: [2, 4, 4, 4, 5, 5, 7, 9]

1. Calcular la media
2. Calcular la desviación estándar
3. Estandarizar cada valor
4. Verificar que la media sea ~0 y std sea ~1

```python
datosE = [2, 4, 4, 4, 5, 5, 7, 9]

suma = 0
for i in datosE:
    suma = suma + i

μ = suma / len(datosE)
suma_cuadrados = sum([(x - μ) ** 2 for x in datosE])
calc_var = suma_cuadrados / (len(datosE) - 1)
σ = calc_var**0.5
Z = lambda X: (X - μ) / σ
resultado_estandarizacion = [Z(x) for x in datosE]

print(f"Datos para estandarizar: {datosE}")
print(f"Media: {μ}")
print(f"Desviacion estandar: {σ}")
print(f"Estandarización de cada dato: {resultado_estandarizacion}")
```

#### Ejercicio 3: Comparación de Técnicas

```python
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler

datos = np.array([100, 200, 300, 400, 500]).reshape(-1, 1)

# Aplicar:
# 1. MinMaxScaler de sklearn
# 2. StandardScaler de sklearn
# Comparar resultados

mmScaler = MinMaxScaler()
stScaler = StandardScaler()

scaled_minmax = mmScaler.fit_transform(datos)
scaled_standard = stScaler.fit_transform(datos)

print("\nDatos para comparacion de tecnicas: \n", datos)
print("Escala min-max: \n", scaled_minmax)
print("Escala estandar: \n", scaled_standard)
```

**Comparacion de escalas**
![impresion de ambas escalas en consola](img/datacomp.png)

---

### Ejercicios de Manejo de Valores Faltantes

#### Ejercicio 4: Identificación de Valores Faltantes

```python
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],
    'B': [np.nan, 2, 3, 4, np.nan],
    'C': [1, 2, 3, 4, 5]
})

# Ejercicios:
# 1. Identificar valores faltantes con isnull()
# 2. Contar valores faltantes por columna
# 3. Calcular porcentaje de valores faltantes
# 4. Mostrar solo filas con valores faltantes

print(df.isnull())
faltantes = df.isnull().sum()
print(faltantes)
porcen_valor = (faltantes * len(df)) / 100
print(porcen_valor)
print(df[df.isnull().any(axis=1)])
```

#### Ejercicio 5: Estrategias de Imputación

```python
# Para el mismo DataFrame, aplicar:
# 1. Eliminar filas con valores faltantes
# 2. Eliminar columnas con valores faltantes
# 3. Imputar con la media
# 4. Imputar con la mediana
# 5. Imputar con forward fill
# 6. Imputar con backward fill

df_drop_rows = df.dropna()
df_drop_cols = df.dropna(axis=1)
df_mean = df.fillna(df.mean())
df_median = df.fillna(df.median())
df_ffill = df.ffill()
df_bfill = df.bfill()

print("Original:\n", df)
print("\nCon Media:\n", df_mean)
print("\nForward Fill:\n", df_ffill)
```

#### Ejercicio 6: Imputación Avanzada

```python
# Usar sklearn.impute.SimpleImputer
from sklearn.impute import SimpleImputer

# Probar diferentes estrategias:
# - mean
# - median
# - most_frequent
# - constant

estrategias = ['mean', 'median', 'most_frequent', 'constant']
for est in estrategias:
    if est == 'constant':
        imputer = SimpleImputer(strategy=est, fill_value=-1)
    else:
        imputer = SimpleImputer(strategy=est)
    datos_imputados = imputer.fit_transform(df)
    df_result = pd.DataFrame(datos_imputados, columns=df.columns)

    print(f"\n--- Estrategia: {est} ---")
    print(df_result)
```

---

### Ejercicios de Detección y Manejo de Outliers

#### Ejercicio 7: Método IQR (Rango Intercuartil)

```python
import numpy as np
datos = [10, 12, 14, 15, 16, 18, 20, 22, 25, 100]

# Calcular:
# 1. Q1 (percentil 25)
# 2. Q3 (percentil 75)
# 3. IQR = Q3 - Q1
# 4. Límite inferior = Q1 - 1.5 * IQR
# 5. Límite superior = Q3 + 1.5 * IQR
# 6. Identificar outliers

q1 = np.percentile(datos, 25)
print("Q1: ", q1)

q3 = np.percentile(datos, 75)
print("Q3: ", q3)

iqr = q3 - q1
print(iqr)

linf = q1 - 1.5 * iqr
lins = q3 + 1.5 * iqr
print("Límite inferior: ", linf)
print("Limite superior: ", lins)

outliers = [x for x in datos if x < linf or x > lins]
print("Outliers: ", outliers)
```

#### Ejercicio 8: Método Z-Score

```python
from scipy import stats
import numpy as np

datos = np.array([10, 12, 14, 15, 16, 18, 20, 22, 25, 100])

# Calcular Z-scores y encontrar valores donde |Z| > 3
z_scores = stats.zscore(datos)
outliers = np.where(np.abs(z_scores) > 3)
print(f"Outliers detectados: {outliers}")
```

#### Ejercicio 9: Manejo de Outliers

```python
from scipy import stats
# Opciones para manejar outliers:
# 1. Eliminar outliers
# 2.替换为边界值 (capping)
# 3. Transformación logarítmica
# 4. Transformación Box-Cox
# Aplicar cada método

q1, q3 = np.percentile(datos, [25, 75])
iqr = q3 - q1
inf, sup = q1 - 1.5 * iqr, q3 + 1.5 * iqr
datos_limpios = datos[(datos >= inf) & (datos <= sup)]
print(f"Sin outliers: {datos_limpios}")
datos_capping = np.clip(datos, inf, sup)
print(f"Con Capping: {datos_capping}")
datos_log = np.log1p(datos)
print(f"Transformación Logarítmica: {datos_log}")
datos_bc, lmbda = stats.boxcox(datos)
print(f"Lambda óptimo: {lmbda:.4f}")
print(f"Transformación Box-Cox: {datos_bc}")
```

---

### Ejercicios de Transformación de Variables

#### Ejercicio 10: Codificación de Variables Categóricas

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.DataFrame({
    'color': ['rojo', 'azul', 'verde', 'rojo', 'verde'],
    'talla': ['S', 'M', 'L', 'S', 'M']
})

# Aplicar:
# 1. Label Encoding
# 2. One-Hot Encoding con get_dummies
# 3. One-Hot Encoding con sklearn

df_label = df.copy()
le = LabelEncoder()
df_label["color_encoded"] = le.fit_transform(df["color"])
print("Label Encoding: \n", df_label)
df_dummies = pd.get_dummies(df, columns=["color"], prefix="color")
print("\nPandas get_dummies: \n", df_dummies)
ohe = OneHotEncoder(sparse_output=False)
color_ohe = ohe.fit_transform(df[["color"]])
df_ohe = pd.DataFrame(color_ohe, columns=ohe.get_feature_names_out(["color"]))
print("\nScikit-Learn OneHotEncoder: \n", df_ohe)
```

#### Ejercicio 11: Transformaciones Numéricas

```python
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.preprocessing import KBinsDiscretizer

datos = [1, 2, 3, 4, 5, 10, 20, 30]

# Aplicar:
# 1. Logaritmo natural
# 2. Raíz cuadrada
# 3. Transformación Box-Cox
# 4. Discretización (binned)

datos_log = np.log1p(datos)
datos_sqrt = np.sqrt(datos)
datos_bc, lmbda = stats.boxcox(datos)

kbd = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
datos_binned = kbd.fit_transform(datos.reshape(-1, 1))

df_transform = pd.DataFrame({
    'Original': datos,
    'Log(x+1)': np.round(datos_log, 3),
    'Sqrt': np.round(datos_sqrt, 3),
    'Box-Cox': np.round(datos_bc, 3),
    'Binned': datos_binned.flatten()
})

print(df_transform)
print(f"\nLambda óptimo para Box-Cox: {lmbda:.4f}")
```

#### Ejercicio 12: Feature Engineering

```python
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

# Crear nuevas features:
# 1. Ratio entre dos columnas
# 2. Diferencia entre columnas
# 3. Agregar indicadores binarios
# 4. Polynomial features
# 5. DateTime features

df = pd.DataFrame(
    {
        "ventas": [100, 200, 150, 300],
        "costos": [80, 150, 120, 200],
        "stock": [10, 0, 5, 0],
        "fecha": pd.to_datetime(
            ["2026-04-01", "2026-04-02", "2026-04-03", "2026-04-04"]
        ),
    }
)

df["ratio_beneficio"] = df["ventas"] / df["costos"]

df["ganancia_neta"] = df["ventas"] - df["costos"]

df["sin_stock"] = (df["stock"] == 0).astype(int)

df["dia_semana"] = df["fecha"].dt.dayofweek
df["es_fin_de_semana"] = df["dia_semana"].isin([5, 6]).astype(int)

poly = PolynomialFeatures(degree=2, include_bias=False)
poly_data = poly.fit_transform(df[["ventas", "costos"]])
poly_cols = poly.get_feature_names_out(["ventas", "costos"])
df_poly = pd.DataFrame(poly_data, columns=poly_cols)

df_final = pd.concat([df, df_poly.drop(columns=["ventas", "costos"])], axis=1)

print(df_final.T)
```

---

### Ejercicios de Escalamiento de Datos

#### Ejercicio 13: Comparar Escaladores

```python
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler
import numpy as np

data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Aplicar cada escalador y comparar resultados
# ¿Cuándo usar cada uno?

scalers = {
    "MinMaxScaler": MinMaxScaler(),
    "StandardScaler": StandardScaler(),
    "RobustScaler": RobustScaler(),
    "MaxAbsScaler": MaxAbsScaler()
}

results = {}
for name, scaler in scalers.items():
    results[name] = scaler.fit_transform(data)[:, 0]

df_comp = pd.DataFrame(results)
df_comp.insert(0, "Original", data[:, 0])
print(df_comp)
```

**MinMaxScaler**:Cuando los datos no tienen outliers y necesitas que todas las variables tengan la misma escala exacta
**StandardScaler**:Se usa en Regresión Logística, SVM o PCA. Asume que tus datos tienen una distribución normal
**RobustScaler**:Cuando tus datos tienen muchos outliers. Como usa la mediana, los valores extremos no jalan el escalado de los demás datos.
**MaxAbsScaler**:Diseñado específicamente para datos dispersos, como matrices llenas de ceros de procesamiento de texto

#### Ejercicio 14: Pipeline de Preprocesamiento

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer

# Crear un pipeline completo:
# 1. Seleccionar columnas numéricas y categóricas
# 2. Aplicar transformaciones apropiadas
# 3. Combinar en un pipeline

df = pd.DataFrame({
    'edad': [25, 30, np.nan, 45, 20],
    'salario': [50000, 80000, 60000, np.nan, 30000],
    'ciudad': ['Madrid', 'Paris', 'Madrid', 'Londres', 'Paris'],
    'compro': ['No', 'Si', 'Si', 'No', 'Si']
})

num_features = ['edad', 'salario']
cat_features = ['ciudad']

num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())                    
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore')) 
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, num_features),
        ('cat', cat_transformer, cat_features)
    ]
)

full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor)
])

df_processed = full_pipeline.fit_transform(df)

print("Datos procesados (Numpy Array):")
print(df_processed)
```

---

### Ejercicios de Investigación

#### Ejercicio 15: Mejores Prácticas

Investigar:

1. ¿Por qué es importante la preparación de datos?:  Es importante la preparacion de datos por que Los valores faltantes o errores de captura sesgan las predicciones. Limpiar los datos asegura que el modelo aprenda patrones reales y no errores aleatorios.
2. ¿Qué es data leakage y cómo evitarlo?:  Ocurre cuando información del futuro o del conjunto de datos que el modelo "no debería ver" se filtra en el proceso de entrenamiento y para evitarlo primero se hace el train_test_split y luego calcula medias o escalas basadas solo en el conjunto de entrenamiento.
3. ¿Cuál es la diferencia entre datos de entrenamiento y prueba?:  El entrenamiento son los ejercicios del libro que tiene la respuesta final, prueba son el examen final y son datos que el modelo nunca ha visto

#### Ejercicio 16: Técnicas Avanzadas

Investigar:

1. ¿Qué es SMOTE para datos desbalanceados?:  Se usa cuando tienes un Dataset Desbalanceado el modelo tenderá a ignorar los fraudes porque son muy pocos.
2. ¿Qué es la imputación por K-Nearest Neighbors?:  Es una forma inteligente de rellenar valores faltantes.
3. ¿Qué es Target Encoding?:  Es una técnica de codificación para variables categóricas.

---

## Actividades practicas

---

#### Actividad 4.1: Identificación de Valores Faltantes

**Descripción:** Aprende a detectar y manejar valores faltantes.

**Instrucciones:**

1. Crea un DataFrame con valores nulos
2. Practica diferentes métodos de detección:
   - isnull() / notnull()
   - sum() para contar nulos por columna
   - info() para ver completitud
3. Investiga diferentes estrategias de manejo
4. Aplica al menos 3 técnicas diferentes

---

#### Actividad 4.2: Imputación de Datos

**Descripción:** Practica técnicas de imputación de datos.

**Instrucciones:**

1. Usa un dataset con valores nulos
2. Aplica las siguientes técnicas de imputación:
   - Imputación por media
   - Imputación por mediana
   - Imputación por moda
   - Imputación hacia adelante/atrás
3. Compara los resultados
4. Justifica cuándo usar cada método

---

#### Actividad 4.3: Transformación de Datos

**Descripción:** Practica transformaciones comunes de datos.

**Instrucciones:**

1. Con un dataset, realiza las siguientes transformaciones:
   - Normalización de datos (Min-Max)
   - Estandarización (Z-score)
   - Codificación de variables categóricas (One-Hot Encoding)
   - Creación de variables derivadas
2. Explica cada transformación y cuándo usarla

---

#### Actividad 4.4: Pipeline de Procesamiento

**Descripción:** Crea un pipeline completo de procesamiento.

**Instrucciones:**

1. Diseña un pipeline que incluya:
   - Carga de datos
   - Manejo de valores nulos
   - Transformación de variables
   - Selección de características
2. Usa sklearn Pipeline si es posible
3. Documenta cada paso

---

## Ejercicios extras en clase - Procesamiento de datos en python

---

### Map y filter

#### Ejercicio 1

```python
# map(): Duplicar numeros usando funcion y lambda
numeros = [1, 2, 3, 4, 5]
# Completar con map(duplicar, numeros) y map(lambda x: x*2, numeros)
```

#### Ejercicio 2

```python
# map(): Duplicar numeros usando funcion y lambda
numeros = [1, 2, 3, 4, 5]
# Completar con map(duplicar, numeros) y map(lambda x: x*2, numeros)
```

#### Ejercicio 3

```python
# map(): Duplicar numeros usando funcion y lambda
numeros = [1, 2, 3, 4, 5]
# Completar con map(duplicar, numeros) y map(lambda x: x*2, numeros)
```

---

### Lambda

#### Ejercicio 1

```python
# Lambda basicas: cuadrado, suma, maximo
# Completar: cuadrado = lambda ... ; suma = lambda ... ; maximo = lambda ...
```

#### Ejercicio 2

```python
# sorted() con lambda: ordenar por edad y por nombre (desc)
personas = [("Ana", 25), ("Carlos", 30), ("Beatriz", 22)]
# Completar: sorted(personas, key=...)
```

#### Ejercicio 3

```python
# max() y min() con lambda: mayor y menor edad
personas = [{"nombre": "Ana", "edad": 25}, {"nombre": "Carlos", "edad": 30}]
# Completar: max(..., key=...), min(..., key=...)
```

---

### NumPy

#### Ejercicio 1

```python
# Sin NumPy: suma con bucle for
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
# Completar: bucle for para sumar elementos
```

#### Ejercicio 2

```python
# Con NumPy: operaciones +, -, *, /
a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
# Completar: a+b, a-b, a*b, b/a
```

#### Ejercicio 3

```python
# Funciones NumPy: sqrt, mean, std, median
a = np.array([1, 2, 3, 4, 5])
# Completar: np.sqrt(a), np.mean(a), np.std(a), np.median(a)
```

---

### Limpieza de datos

#### Ejercicio 1

```python
# Crear DataFrame con valores nulos
data = {'nombre': ['Juan', 'Maria', None, 'Ana'], 'edad': [25, None, 30], 'salario': [50000, None, 48000]}
df = pd.DataFrame(data)
print(df)
```

#### Ejercicio 2

```python
# Deteccion de nulos: isnull().sum()
# Completar: df.isnull().sum()
```

#### Ejercicio 3

```python
# Estrategias: dropna() y fillna()
# Completar: df.dropna() y df.fillna(valor)
```

#### Ejercicio 4

```python
# Correccion de tipos: pd.to_numeric(..., errors='coerce')
df = pd.DataFrame({'edad': [25, 'desconocida', 30]})
# Completar: convertir columna edad a numerico
```

---

### Reindexacion

#### Ejercicio 1

```python
# reindex() con fill_value
serie = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
# Completar: serie.reindex(['a','b','c','d'], fill_value=0)
```

#### Ejercicio 2

```python
# reindex en DataFrame: filas y columnas
df = pd.DataFrame({'col1': [1,2,3], 'col2': [4,5,6]}, index=['x','y','z'])
# Completar: df.reindex(['x','y','z','w']) y df.reindex(columns=[...], fill_value=0)
```

#### Ejercicio 3

```python
# ffill() y bfill()
serie = pd.Series([100, None, 300, None, 500])
# Completar: serie.ffill() y serie.bfill()
```

---

### Apply()

#### Ejercicio 1

```python
# apply() basic: suma por columna
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6], 'c': [7, 8, 9]})
# Completar: df.apply(sum)
```

#### Ejercicio 2

```python
# apply() con axis: axis=0 (columnas), axis=1 (filas)
# Completar: df.apply(max, axis=0) y df.apply(sum, axis=1)
```

#### Ejercicio 3

```python
# apply() con columnas: calcular IMC
df = pd.DataFrame({'peso': [70, 65], 'altura': [1.70, 1.60]})
# Completar: def imc(fila): return... ; df['imc'] = df.apply(..., axis=1)
```

#### Ejercicio 4

```python
# apply() para clasificacion (ej: IMC normal/sobrepeso)
df['categoria'] = df['imc'].apply(lambda x: 'Normal' if x < 25 else 'Sobrepeso')
# Completar: funcion con if/elif/else
```

---

### Merges

#### Ejercicio 1

```python
# DataFrames para merge
# DataFrame de empleados
empleados = pd.DataFrame({'id_empleado': [1, 2, 3, 4],'nombre': ['Juan', 'Maria', 'Pedro', 'Ana'],'departamento_id': [10, 20, 10, 30]})

# DataFrame de departamentos
departamentos = pd.DataFrame({'departamento_id': [10, 20, 30], 'nombre_dept': ['TI', 'Ventas', 'RH']})
```

#### Ejercicio 2

```python
# INNER JOIN: solo claves en ambas tablas
# Completar: pd.merge(empleados, departamentos, on='dept_id', how='inner')
```

#### Ejercicio 3

```python
# LEFT JOIN: todos de empleados
# Completar: how='left'
```

#### Ejercicio 4

```python
# RIGHT JOIN: todos de departamentos
# Completar: how='right'
```

#### Ejercicio 5

```python
# OUTER JOIN: todos de ambas
# Completar: how='outer'
```

#### Ejercicio 6

```python
# Merge con claves diferentes: left_on, right_on
df1 = pd.DataFrame({'id': [1,2], 'nombre': ['Juan','Maria']})
df2 = pd.DataFrame({'emp_id': [1,3], 'salario': [50000,60000]})
# Completar: pd.merge(df1, df2, left_on='id', right_on='emp_id', how='inner')
```

#### Ejercicio 7

```python
# Merge multiple: encadenar merge()
# Completar: df1.merge(df2, on='...').merge(df3, on='...')
```

---

### Ejercicios

#### Ejercicio 1

```python
# 1. temps = [15,22,30,18,25] -> Fahrenheit y filtrar >20
```

#### Ejercicio 2

```python
# 2. personas = [{'nombre':'Ana','edad':25},{'nombre':'Carlos','edad':30}] -> ordenar por edad, max
```

#### Ejercicio 3

```python
# 3. NumPy: a=np.array([1,2,3,4,5]), b=np.array([10,20,30,40,50]) -> +,-,*,/ y media,std
```

#### Ejercicio 4

```python
# 4. df con nulos -> dropna, fillna, ffill
```

#### Ejercicio 5

```python
# 5. serie.reindex(['a','b','c','d'], fill_value=0), ffill, bfill
```

#### Ejercicio 6

```python
# 6. df(precio,cantidad) -> apply(lambda x: x['precio']*x['cantidad'], axis=1)
```

#### Ejercicio 7

```python
# 7. df1,df2 -> inner, left, right, outer
```
