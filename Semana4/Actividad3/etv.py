import pandas as pd
from sklearn.preprocessing import (
    LabelEncoder,
    OneHotEncoder,
    KBinsDiscretizer,
    PolynomialFeatures,
)
import numpy as np
from scipy import stats

df = pd.DataFrame(
    {
        "color": ["rojo", "azul", "verde", "rojo", "verde"],
        "talla": ["S", "M", "L", "S", "M"],
    }
)

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


datos = np.array([1, 2, 3, 4, 5, 10, 20, 30])

# Aplicar:
# 1. Logaritmo natural
# 2. Raíz cuadrada
# 3. Transformación Box-Cox
# 4. Discretización (binned)

datos_log = np.log1p(datos)
datos_sqrt = np.sqrt(datos)
datos_bc, lmbda = stats.boxcox(datos)

kbd = KBinsDiscretizer(n_bins=3, encode="ordinal", strategy="uniform")
datos_binned = kbd.fit_transform(datos.reshape(-1, 1))

df_transform = pd.DataFrame(
    {
        "Original": datos,
        "Log(x+1)": np.round(datos_log, 3),
        "Sqrt": np.round(datos_sqrt, 3),
        "Box-Cox": np.round(datos_bc, 3),
        "Binned": datos_binned.flatten(),
    }
)

print(df_transform)
print(f"\nLambda óptimo para Box-Cox: {lmbda:.4f}")

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
