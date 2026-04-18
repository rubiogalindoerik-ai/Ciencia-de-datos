import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

df = pd.DataFrame(
    {"A": [1, 2, np.nan, 4, 5], "B": [np.nan, 2, 3, 4, np.nan], "C": [1, 2, 3, 4, 5]}
)

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

# Probar diferentes estrategias:
# - mean
# - median
# - most_frequent
# - constant

estrategias = ["mean", "median", "most_frequent", "constant"]
for est in estrategias:
    if est == "constant":
        imputer = SimpleImputer(strategy=est, fill_value=-1)
    else:
        imputer = SimpleImputer(strategy=est)
    datos_imputados = imputer.fit_transform(df)
    df_result = pd.DataFrame(datos_imputados, columns=df.columns)

    print(f"\n--- Estrategia: {est} ---")
    print(df_result)
