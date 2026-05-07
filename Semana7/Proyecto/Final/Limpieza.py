import pandas as pd

df = pd.read_csv("Datos/train2.csv")

# Llenamos con la mediana
columnas_a_imputar = ["bedrooms", "bathrooms", "beds"]
for col in columnas_a_imputar:
    df[col] = df[col].fillna(df[col].median())

# 2. Selección de columnas relevantes
columnas_relevantes = [
    "log_price",
    "accommodates",
    "bathrooms",
    "bedrooms",
    "beds",
    "number_of_reviews",
    "review_scores_rating",
]

# columnas elegidas y eliminamos filas con nulos
df_limpio = df[columnas_relevantes].dropna().copy()

# Guardamos el archivo
df_limpio.to_csv("Datos/train2_limpio.csv", index=False)

print(f"Nulos restantes: {df_limpio.isnull().sum().sum()}")
print("Archivo limpio guardado.")

