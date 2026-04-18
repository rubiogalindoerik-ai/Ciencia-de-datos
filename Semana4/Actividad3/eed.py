from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    RobustScaler,
    MaxAbsScaler,
    OneHotEncoder,
)
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

# Aplicar cada escalador y comparar resultados
# ¿Cuándo usar cada uno?

scalers = {
    "MinMaxScaler": MinMaxScaler(),
    "StandardScaler": StandardScaler(),
    "RobustScaler": RobustScaler(),
    "MaxAbsScaler": MaxAbsScaler(),
}

results = {}
for name, scaler in scalers.items():
    # Solo mostramos la primera columna para comparar
    results[name] = scaler.fit_transform(data)[:, 0]

df_comp = pd.DataFrame(results)
df_comp.insert(0, "Original", data[:, 0])
print(df_comp)

# Crear un pipeline completo:
# 1. Seleccionar columnas numéricas y categóricas
# 2. Aplicar transformaciones apropiadas
# 3. Combinar en un pipeline

df = pd.DataFrame(
    {
        "edad": [25, 30, np.nan, 45, 20],
        "salario": [50000, 80000, 60000, np.nan, 30000],
        "ciudad": ["Madrid", "Paris", "Madrid", "Londres", "Paris"],
        "compro": ["No", "Si", "Si", "No", "Si"],
    }
)

num_features = ["edad", "salario"]
cat_features = ["ciudad"]

num_transformer = Pipeline(
    steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
)

cat_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", num_transformer, num_features),
        ("cat", cat_transformer, cat_features),
    ]
)

full_pipeline = Pipeline(steps=[("preprocessor", preprocessor)])

df_processed = full_pipeline.fit_transform(df)

print("Datos procesados (Numpy Array):")
print(df_processed)
